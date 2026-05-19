"""
Generate report tables from the analysis output.

This script creates all the summary tables used in the Word document reports
and saves them as CSVs, images, and HTML for easy use in documents.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Output directory
output_dir = Path(__file__).parent.parent / "outputs"
output_dir.mkdir(exist_ok=True)

# Full set of cleaned game CSVs used in the analysis notebooks.
GAME_SPECS = [
    {"name": "Palworld", "file": "../data:clean/palworld_2024-12-09_to_2025-01-13.csv", "update": "2024-12-23"},
    {"name": "Warframe", "file": "../data:clean/warframe_2025-11-26_to_2025-12-31.csv", "update": "2025-12-10"},
    {"name": "Counter-Strike 2", "file": "../data:clean/counter_strike_2_2024-04-23_to_2024-05-28.csv", "update": "2024-05-07"},
    {"name": "Sea of Thieves", "file": "../data:clean/sea_of_thieves_2024-10-03_to_2024-11-07.csv", "update": "2024-10-17"},
    {"name": "PUBG: BATTLEGROUNDS", "file": "../data:clean/pubg__battlegrounds_2025-10-22_to_2025-11-26.csv", "update": "2025-11-05"},
    {"name": "Dead by Daylight", "file": "../data:clean/dead_by_daylight_2023-11-14_to_2023-12-19.csv", "update": "2023-11-28"},
    {"name": "Don't Starve Together", "file": "../data:clean/don_t_starve_together_2023-04-13_to_2023-05-18.csv", "update": "2023-04-27"},
    {"name": "Deep Rock Galactic", "file": "../data:clean/deep_rock_galactic_2024-05-30_to_2024-07-04.csv", "update": "2024-06-13"},
    {"name": "Apex Legends", "file": "../data:clean/apex_legends_2025-01-28_to_2025-03-04.csv", "update": "2025-02-11"},
    {"name": "Destiny 2", "file": "../data:clean/destiny_2_2024-09-24_to_2024-10-29.csv", "update": "2024-10-08"},
    {"name": "No Man's Sky", "file": "../data:clean/no_man_s_sky_2025-01-15_to_2025-02-19.csv", "update": "2025-01-29"},
    {"name": "HELLDIVERS 2", "file": "../data:clean/helldivers_2_2025-08-19_to_2025-09-23.csv", "update": "2025-09-02"},
    {"name": "Path of Exile", "file": "../data:clean/path_of_exile_2025-06-06_to_2025-07-04.csv", "update": "2025-06-13"},
    {"name": "Rainbow Six Siege", "file": "../data:clean/rainbow_six_siege_2024-08-19_to_2024-09-16.csv", "update": "2024-08-26"},
    {"name": "The Finals", "file": "../data:clean/the_finals_2024-12-05_to_2025-01-02.csv", "update": "2024-12-12"},
    {"name": "V Rising", "file": "../data:clean/v_rising_2025-04-21_to_2025-05-19.csv", "update": "2025-04-28"},
]


def load_game_frame(game_spec, standardize=False):
    """Load and prepare one game CSV."""
    df = pd.read_csv(Path(__file__).parent / game_spec["file"])
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    df = df.sort_values("DateTime").reset_index(drop=True)

    if standardize:
        df["Players_scaled"] = (df["Players"] - df["Players"].mean()) / df["Players"].std()

    return df


def build_summary_stats(game_specs):
    rows = []
    for game in game_specs:
        df = load_game_frame(game)
        rows.append(
            {
                "Game": game["name"],
                "Observations": int(len(df)),
                "Mean players": float(df["Players"].mean()),
                "Std. dev.": float(df["Players"].std()),
                "Min": float(df["Players"].min()),
                "Max": float(df["Players"].max()),
            }
        )

    return pd.DataFrame(rows)


def compute_segment_slope(segment, value_column):
    """Compute a simple linear slope for a time segment."""
    if segment.empty or len(segment) <= 1:
        return 0.0

    segment = segment.copy()
    segment["DayIndex"] = (segment["DateTime"] - segment["DateTime"].min()).dt.days

    try:
        return float(np.polyfit(segment["DayIndex"], segment[value_column], 1)[0])
    except Exception:
        return 0.0


def build_before_after_changes(game_specs):
    rows = []
    for game in game_specs:
        df = load_game_frame(game, standardize=True)
        update_date = pd.to_datetime(game["update"])

        before_df = df[(df["DateTime"] >= update_date - pd.Timedelta(days=7)) & (df["DateTime"] <= update_date - pd.Timedelta(days=1))].copy()
        after_df = df[df["DateTime"] >= update_date].copy()

        avg_before = float(before_df["Players_scaled"].mean()) if not before_df.empty else float("nan")
        avg_after = float(after_df["Players_scaled"].mean()) if not after_df.empty else float("nan")

        rows.append(
            {
                "Game": game["name"],
                "Avg. before": avg_before,
                "Avg. after": avg_after,
                "Change": avg_after - avg_before if pd.notna(avg_before) and pd.notna(avg_after) else float("nan"),
            }
        )

    return pd.DataFrame(rows)


def build_trend_analysis_results(game_specs):
    rows = []
    for game in game_specs:
        df = load_game_frame(game, standardize=True)
        update_date = pd.to_datetime(game["update"])

        before_df = df[(df["DateTime"] >= update_date - pd.Timedelta(days=7)) & (df["DateTime"] <= update_date - pd.Timedelta(days=1))].copy()
        after_df = df[df["DateTime"] >= update_date].copy()

        avg_before = float(before_df["Players_scaled"].mean()) if not before_df.empty else float("nan")
        avg_after = float(after_df["Players_scaled"].mean()) if not after_df.empty else float("nan")

        if pd.notna(avg_before) and avg_before > 0:
            pct_change = ((avg_after - avg_before) / avg_before) * 100
        else:
            pct_change = float("inf")

        full_df = df.copy()
        full_df["DayIndex"] = (full_df["DateTime"] - full_df["DateTime"].min()).dt.days
        trend_slope = float(np.polyfit(full_df["DayIndex"], full_df["Players_scaled"], 1)[0]) if len(full_df) > 1 else 0.0

        rows.append(
            {
                "Game": game["name"],
                "Avg Players Before": avg_before,
                "Avg Players After": avg_after,
                "Percentage Change (%)": pct_change,
                "Trend Slope": trend_slope,
            }
        )

    return pd.DataFrame(rows)

# ============================================================================
# TABLE 1: Sample Construction
# ============================================================================

sample_construction = pd.DataFrame({
    'Step': [
        'Initial cleaned game files',
        'Outcome construction',
        'Event-time alignment',
        'Main event-study window',
        'Reference period'
    ],
    'Description': [
        'Daily observations for all 16 cleaned multiplayer games around major update dates',
        'Standardize player counts within each game to create comparable z-scores',
        'Convert dates into days relative to the update date',
        'Use observations in the dynamic +/-14 day window',
        'Omit day -1 from the event-study dummies'
    ],
    'Result': [
        '548 observations across 16 games',
        'Players_scaled',
        'day k, where k = 0 is update day',
        '436 observations',
        'Coefficients are relative to the day before update'
    ]
})

# ============================================================================
# TABLE 2: Variable Definitions
# ============================================================================

variable_definitions = pd.DataFrame({
    'Variable': [
        'Players',
        'Players_scaled',
        'day_k',
        'post_update',
        'is_coop',
        'post_update x is_coop'
    ],
    'Meaning': [
        'Raw daily player count',
        'Within-game standardized player count',
        'Dummy for day k relative to update',
        'Indicator equal to 1 after the update',
        'Indicator for co-op/PvE game classification',
        'Interaction between post-update and co-op status'
    ],
    'Use in analysis': [
        'Original engagement measure',
        'Main regression outcome',
        'Dynamic event-study coefficients',
        'Average before-after comparison',
        'Heterogeneity check',
        'Tests whether co-op games respond differently'
    ]
})

summary_stats = build_summary_stats(GAME_SPECS)

# Round for a cleaner report-ready table while preserving the underlying data.
summary_stats['Mean players'] = summary_stats['Mean players'].round(2)
summary_stats['Std. dev.'] = summary_stats['Std. dev.'].round(2)
summary_stats['Min'] = summary_stats['Min'].round(2)
summary_stats['Max'] = summary_stats['Max'].round(2)

# ============================================================================
# TABLE 4: Main Event-Study Coefficients
# ============================================================================

event_study_coeffs = pd.DataFrame({
    'Event time': [
        'Day -7',
        'Day -2',
        'Day 0',
        'Day 1',
        'Day 3',
        'Day 7',
        'Day 14'
    ],
    'Coefficient': [-0.2916, 0.1080, 1.6367, 1.6533, 1.9076, 1.2412, 0.5423],
    'Std. error': [0.2617, 0.2617, 0.2617, 0.2617, 0.2617, 0.2617, 0.2617],
    '95% CI Low': [-0.806, -0.406, 1.122, 1.139, 1.393, 0.727, 0.028],
    '95% CI High': [0.223, 0.622, 2.151, 2.168, 2.422, 1.756, 1.057],
    'Interpretation': [
        'No evidence of large pre-update spike',
        'Close to baseline before update',
        'Large immediate update-day increase',
        'Effect continues after update',
        'Peak response in the event window',
        'Effect remains positive one week later',
        'Effect fades but remains positive'
    ]
})

before_after_changes = build_before_after_changes(GAME_SPECS)
before_after_changes['Avg. before'] = before_after_changes['Avg. before'].round(2)
before_after_changes['Avg. after'] = before_after_changes['Avg. after'].round(2)
before_after_changes['Change'] = before_after_changes['Change'].round(2)

trend_analysis_results = build_trend_analysis_results(GAME_SPECS)
trend_analysis_results['Avg Players Before'] = trend_analysis_results['Avg Players Before'].round(2)
trend_analysis_results['Avg Players After'] = trend_analysis_results['Avg Players After'].round(2)
trend_analysis_results['Percentage Change (%)'] = trend_analysis_results['Percentage Change (%)'].round(2)
trend_analysis_results['Trend Slope'] = trend_analysis_results['Trend Slope'].round(2)

# ============================================================================
# TABLE 6: Robustness Checks
# ============================================================================

robustness_checks = pd.DataFrame({
    'Specification': [
        'Main event study',
        'No controls',
        'Game fixed effects',
        'Drop outliers',
        'Low-volatility games',
        'PvP only',
        'Co-op only',
        'HC3 robust SE',
        'Clustered SE',
        'Bootstrap',
        'Placebo day -7',
        'Placebo day -14'
    ],
    'Day 0 coeff.': [
        1.6367, 1.6367, 1.6367, 1.6367, 1.2537, 1.2710, 1.9763,
        1.6367, 1.6367, 1.6291, 0.1271, -0.3108
    ],
    'Std. error': [
        0.2617, 0.2617, 0.2594, 0.2617, 0.3128, 0.5312, 0.2746,
        0.3990, 0.4363, 0.3843, 0.3021, 0.2826
    ],
    '95% CI Low': [
        1.1223, 1.1223, 1.1267, 1.1223, 0.6382, 0.2174, 1.4323,
        0.8546, 0.7815, 0.8728, None, None
    ],
    '95% CI High': [
        2.1510, 2.1510, 2.1467, 2.1510, 1.8692, 2.3247, 2.5203,
        2.4187, 2.4919, 2.3708, None, None
    ],
    'N': [436, 436, 436, 436, 341, 131, 145, 436, 436, 436, 436, 436],
    'Interpretation': [
        'Baseline estimate',
        'Unchanged without control labels',
        'Stable after absorbing game-level differences',
        'Holds when outliers removed',
        'Smaller but still positive',
        'Positive in competitive games',
        'Larger in co-op sample',
        'Robust to heteroskedasticity',
        'Robust to within-game clustering',
        'Similar under resampling',
        'No fake pre-update effect',
        'No fake pre-update effect'
    ]
})

# ============================================================================
# Save all tables to CSV
# ============================================================================

sample_construction.to_csv(output_dir / 'sample_construction.csv', index=False)
variable_definitions.to_csv(output_dir / 'variable_definitions.csv', index=False)
summary_stats.to_csv(output_dir / 'Table_1_Summary_Statistics.csv', index=False)
event_study_coeffs.to_csv(output_dir / 'Table_2_Event_Study_Coefficients.csv', index=False)
before_after_changes.to_csv(output_dir / 'Table_3_Before_After_Changes.csv', index=False)
robustness_checks.to_csv(output_dir / 'Table_4_Robustness_Checks.csv', index=False)

# Keep the standalone trend markdown files synchronized with the expanded tables.
# Export event study coefficients as HTML table
event_study_coeffs.to_html(output_dir / 'Table_2_Event_Study_Coefficients.html', index=False)

# Keep the standalone trend markdown files synchronized with the expanded tables.
before_after_markdown = "## Player Trend Analysis: Before vs. After Update\n\n"
before_after_markdown += "| Game | Avg Players Before | Avg Players After | Pct Change (%) | Slope Before | Slope After |\n"
before_after_markdown += "|------|--------------------|-------------------|----------------|--------------|-------------|\n"

for game in GAME_SPECS:
    df = load_game_frame(game, standardize=True)
    update_date = pd.to_datetime(game["update"])
    before_df = df[(df["DateTime"] >= update_date - pd.Timedelta(days=7)) & (df["DateTime"] <= update_date - pd.Timedelta(days=1))].copy()
    after_df = df[df["DateTime"] >= update_date].copy()

    avg_before = float(before_df["Players_scaled"].mean()) if not before_df.empty else float("nan")
    avg_after = float(after_df["Players_scaled"].mean()) if not after_df.empty else float("nan")
    pct_change = ((avg_after - avg_before) / avg_before) * 100 if pd.notna(avg_before) and avg_before > 0 else float("inf")
    slope_before = compute_segment_slope(before_df, "Players_scaled")
    slope_after = compute_segment_slope(after_df, "Players_scaled")

    before_after_markdown += (
        f"| {game['name']} | {avg_before:.2f} | {avg_after:.2f} | "
        f"{pct_change:.2f} | {slope_before:.2f} | {slope_after:.2f} |\n"
    )

(output_dir / 'before_after_trend_analysis.md').write_text(before_after_markdown, encoding='utf-8')

trend_markdown = "## Player Trend Analysis Results\n\n"
trend_markdown += "| Game | Avg Players Before | Avg Players After | Percentage Change (%) | Trend Slope |\n"
trend_markdown += "|------|--------------------|-------------------|-----------------------|-------------|\n"

for _, row in trend_analysis_results.iterrows():
    trend_markdown += (
        f"| {row['Game']} | {row['Avg Players Before']:.2f} | {row['Avg Players After']:.2f} | "
        f"{row['Percentage Change (%)']:.2f} | {row['Trend Slope']:.2f} |\n"
    )

(output_dir / 'trend_analysis_results.md').write_text(trend_markdown, encoding='utf-8')

print("✓ All tables saved to CSV")

# ============================================================================
# Function to create table images
# ============================================================================

def create_table_image(df, title, filename, figsize=(14, None), dpi=300):
    """Create and save a formatted table as an image."""
    
    # Auto-calculate height based on row count
    if figsize[1] is None:
        height = max(4, 0.4 * len(df) + 1.5)
        figsize = (figsize[0], height)
    
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    ax.axis('off')
    fig.patch.set_facecolor('white')
    
    # Add title (skip if empty)
    if title and title.strip():
        fig.suptitle(title, fontsize=16, fontweight='bold', y=0.98)
        pad = 0.95
    else:
        pad = 0.99
    
    # Create table
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc='center',
        colLoc='center',
        loc='center'
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.8)
    
    # Style the table
    header_color = '#1f3b4d'
    row_alt_color = '#f4f7fa'
    border_color = '#c7d0d9'
    
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(border_color)
        cell.set_linewidth(0.8)
        if row == 0:
            cell.set_facecolor(header_color)
            cell.set_text_props(color='white', weight='bold')
        else:
            if row % 2 == 0:
                cell.set_facecolor(row_alt_color)
    
    plt.tight_layout(rect=[0.01, 0.01, 0.99, pad])
    fig.savefig(output_dir / filename, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ {filename}")

# ============================================================================
# Create table images
# ============================================================================

create_table_image(sample_construction, '', 'sample_construction.png', figsize=(14, None))
create_table_image(variable_definitions, '', 'variable_definitions.png', figsize=(14, None))
create_table_image(summary_stats, '', 'Table_1_Summary_Statistics.png', figsize=(14, None))
create_table_image(event_study_coeffs, '', 'Table_2_Event_Study_Coefficients.png', figsize=(18, None))
create_table_image(before_after_changes, '', 'Table_3_Before_After_Changes.png', figsize=(14, None))
create_table_image(robustness_checks, '', 'Table_4_Robustness_Checks.png', figsize=(16, None))

print("\n" + "="*60)
print("All tables generated successfully!")
print("="*60)
print(f"\nCSV files saved to: {output_dir}")
print(f"PNG images saved to: {output_dir}")
