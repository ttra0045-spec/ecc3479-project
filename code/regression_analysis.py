"""Regenerate pooled regression tables (Model 1 and Model 2) as markdown.

This script mirrors the logic in the notebook but is runnable as a script
so outputs stay in sync with the cleaned CSVs.
"""
import pandas as pd
import statsmodels.api as sm
from tabulate import tabulate
import os
from pathlib import Path


def create_regression_table(models, model_names):
    headers = ['Variable'] + model_names
    all_vars = []
    for model in models:
        all_vars.extend(model.params.index.tolist())
    all_vars = sorted(list(set(all_vars)))

    table = []
    for var in all_vars:
        row = [var]
        se_row = ['']
        for model in models:
            if var in model.params.index:
                row.append(f"{model.params[var]:.3f}")
                se_row.append(f"({model.bse[var]:.3f})")
            else:
                row.append('')
                se_row.append('')
        table.append(row)
        table.append(se_row)

    r_squared_row = ['R-squared']
    for model in models:
        r_squared_row.append(f"{model.rsquared:.3f}")
    table.append(r_squared_row)

    n_row = ['N']
    for model in models:
        n_row.append(str(int(model.nobs)))
    table.append(n_row)

    return tabulate(table, headers=headers, tablefmt='pipe')


GAME_SPECS = [
    {"name": "Palworld", "file": "data:clean/palworld_2024-12-09_to_2025-01-13.csv", "update": "2024-12-23"},
    {"name": "Warframe", "file": "data:clean/warframe_2025-11-26_to_2025-12-31.csv", "update": "2025-12-10"},
    {"name": "Counter-Strike 2", "file": "data:clean/counter_strike_2_2024-04-23_to_2024-05-28.csv", "update": "2024-05-07"},
    {"name": "Sea of Thieves", "file": "data:clean/sea_of_thieves_2024-10-03_to_2024-11-07.csv", "update": "2024-10-17"},
    {"name": "PUBG: BATTLEGROUNDS", "file": "data:clean/pubg__battlegrounds_2025-10-22_to_2025-11-26.csv", "update": "2025-11-05"},
    {"name": "Dead by Daylight", "file": "data:clean/dead_by_daylight_2023-11-14_to_2023-12-19.csv", "update": "2023-11-28"},
    {"name": "Don't Starve Together", "file": "data:clean/don_t_starve_together_2023-04-13_to_2023-05-18.csv", "update": "2023-04-27"},
    {"name": "Deep Rock Galactic", "file": "data:clean/deep_rock_galactic_2024-05-30_to_2024-07-04.csv", "update": "2024-06-13"},
    {"name": "Apex Legends", "file": "data:clean/apex_legends_2025-01-28_to_2025-03-04.csv", "update": "2025-02-11"},
    {"name": "Destiny 2", "file": "data:clean/destiny_2_2024-09-24_to_2024-10-29.csv", "update": "2024-10-08"},
    {"name": "No Man's Sky", "file": "data:clean/no_man_s_sky_2025-01-15_to_2025-02-19.csv", "update": "2025-01-29"},
    {"name": "HELLDIVERS 2", "file": "data:clean/helldivers_2_2025-08-19_to_2025-09-23.csv", "update": "2025-09-02"},
    {"name": "Path of Exile", "file": "data:clean/path_of_exile_2025-06-06_to_2025-07-04.csv", "update": "2025-06-13"},
    {"name": "Rainbow Six Siege", "file": "data:clean/rainbow_six_siege_2024-08-19_to_2024-09-16.csv", "update": "2024-08-26"},
    {"name": "The Finals", "file": "data:clean/the_finals_2024-12-05_to_2025-01-02.csv", "update": "2024-12-12"},
    {"name": "V Rising", "file": "data:clean/v_rising_2025-04-21_to_2025-05-19.csv", "update": "2025-04-28"},
]


def main():
    base = Path(__file__).parent.parent
    all_games_df = pd.DataFrame()
    for g in GAME_SPECS:
        # Build an absolute path to the cleaned CSV inside the repository
        csv_path = base / g['file']
        df = pd.read_csv(csv_path)
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        update_date = pd.to_datetime(g['update'])
        df['post_update'] = (df['DateTime'] >= update_date).astype(int)
        df['game'] = g['name']
        all_games_df = pd.concat([all_games_df, df])

    all_games_df['Players_scaled'] = all_games_df.groupby('game')['Players'].transform(lambda x: (x - x.mean()) / x.std())
    all_games_df = all_games_df.dropna(subset=['Players_scaled'])

    # Model 1: Simple OLS
    X1 = sm.add_constant(all_games_df['post_update'])
    y = all_games_df['Players_scaled']
    model1 = sm.OLS(y, X1).fit()

    # Model 2: With Game Fixed Effects
    X2 = pd.get_dummies(all_games_df['post_update'], prefix='post_update', drop_first=True).astype(int)
    X2 = sm.add_constant(X2)
    game_dummies = pd.get_dummies(all_games_df['game'], drop_first=True).astype(int)
    X2 = pd.concat([X2, game_dummies], axis=1)
    model2 = sm.OLS(y, X2).fit()

    # Print key diagnostics so the user can see what was computed
    print('N=', int(model1.nobs))
    print('Model1 post_update=', model1.params['post_update'], 'se=', model1.bse['post_update'])
    print('Model2 post_update_1=', model2.params.get('post_update_1'), 'se=', model2.bse.get('post_update_1'))

    table = create_regression_table([model1, model2], ['Model 1', 'Model 2'])

    output_dir = base / 'outputs'
    os.makedirs(output_dir, exist_ok=True)
    output_path = output_dir / 'regression_table.md'
    with open(output_path, 'w') as f:
        f.write(table)

    print(f'Regression table saved to {output_path}')


if __name__ == '__main__':
    main()
