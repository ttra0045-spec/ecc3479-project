"""
Robustness check utilities for event study analysis.
Provides functions for alternative specifications, outlier detection, 
inference robustness, and summary table generation.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


def get_day_coefficient(model, day):
    """Extract coefficient and confidence interval for a specific day."""
    var_name = f'day_{day}'
    if var_name in model.params.index:
        coeff = model.params[var_name]
        se = model.bse[var_name]
        ci = model.conf_int().loc[var_name]
        return coeff, se, ci[0], ci[1]
    return None, None, None, None


def run_event_study(df, filtered_df, all_control_vars, spec_name="Main"):
    """Run event study model and return model + results dict."""
    event_dummies = pd.get_dummies(filtered_df['days_from_update'], prefix='day')
    if 'day_-1' in event_dummies.columns:
        event_dummies = event_dummies.drop('day_-1', axis=1)
    
    for control in all_control_vars:
        if control in filtered_df.columns:
            event_dummies[control] = filtered_df[control]
    
    y = filtered_df['Players_scaled'].astype(float)
    X = sm.add_constant(event_dummies.astype(float))
    
    model = sm.OLS(y, X).fit()
    
    coeff_0, se_0, ci_low_0, ci_high_0 = get_day_coefficient(model, 0)
    
    results = {
        'spec': spec_name,
        'coeff_day0': coeff_0,
        'se_day0': se_0,
        'ci_low_day0': ci_low_0,
        'ci_high_day0': ci_high_0,
        'n_obs': int(model.nobs),
        'r_squared': model.rsquared,
        'model': model
    }
    
    return model, results


def run_event_study_robust_se(df, filtered_df, all_control_vars, cov_type='HC3', spec_name="Main"):
    """Run event study with alternative covariance estimators."""
    event_dummies = pd.get_dummies(filtered_df['days_from_update'], prefix='day')
    if 'day_-1' in event_dummies.columns:
        event_dummies = event_dummies.drop('day_-1', axis=1)
    
    for control in all_control_vars:
        if control in filtered_df.columns:
            event_dummies[control] = filtered_df[control]
    
    y = filtered_df['Players_scaled'].astype(float)
    X = sm.add_constant(event_dummies.astype(float))
    
    if cov_type == 'cluster':
        model = sm.OLS(y, X).fit(cov_type='cluster', cov_kwds={'groups': filtered_df['game']})
    else:
        model = sm.OLS(y, X).fit(cov_type=cov_type)
    
    coeff_0, se_0, _, _ = get_day_coefficient(model, 0)
    ci = model.conf_int().loc[f'day_0']
    
    results = {
        'spec': spec_name,
        'coeff_day0': coeff_0,
        'se_day0': se_0,
        'ci_low_day0': ci[0],
        'ci_high_day0': ci[1],
        'n_obs': int(model.nobs),
        'r_squared': model.rsquared,
        'model': model
    }
    
    return model, results


def bootstrap_event_study(df, filtered_df, all_control_vars, n_boot=1000, spec_name="Bootstrap"):
    """Run bootstrap for confidence intervals on day 0 coefficient."""
    boot_coefs = []
    n_obs = len(filtered_df)
    
    for _ in range(n_boot):
        idx = np.random.choice(n_obs, n_obs, replace=True)
        boot_sample = filtered_df.iloc[idx].reset_index(drop=True)
        
        event_dummies = pd.get_dummies(boot_sample['days_from_update'], prefix='day')
        if 'day_-1' in event_dummies.columns:
            event_dummies = event_dummies.drop('day_-1', axis=1)
        
        for control in all_control_vars:
            if control in boot_sample.columns:
                event_dummies[control] = boot_sample[control]
        
        y = boot_sample['Players_scaled'].astype(float)
        X = sm.add_constant(event_dummies.astype(float))
        
        try:
            model = sm.OLS(y, X).fit(disp=0)
            if 'day_0' in model.params.index:
                boot_coefs.append(model.params['day_0'])
        except:
            continue
    
    boot_coefs = np.array(boot_coefs)
    
    results = {
        'spec': spec_name,
        'coeff_day0': np.mean(boot_coefs),
        'se_day0': np.std(boot_coefs),
        'ci_low_day0': np.percentile(boot_coefs, 2.5),
        'ci_high_day0': np.percentile(boot_coefs, 97.5),
        'n_obs': len(filtered_df),
        'r_squared': np.nan,
        'boot_coefs': boot_coefs
    }
    
    return results


def remove_outliers_iqr(df, column='Players_scaled', k=1.5):
    """Remove outliers using IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - k * IQR
    upper_bound = Q3 + k * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


def winsorize_by_game(df, column='Players', lower=0.05, upper=0.05):
    """Winsorize player counts by game."""
    df_win = df.copy()
    df_win[column] = df_win[column].astype(float)  # Convert to float to allow winsorizing
    for game in df['game'].unique():
        mask = df['game'] == game
        values = df[mask][column].astype(float)
        lower_val = values.quantile(lower)
        upper_val = values.quantile(1 - upper)
        df_win.loc[mask, column] = np.clip(values.values, lower_val, upper_val)
    
    # Rescale after winsorization
    df_win['Players_scaled'] = df_win.groupby('game')[column].transform(
        lambda x: (x - x.mean()) / x.std()
    )
    return df_win


def detect_influential_obs(model, threshold=0.5):
    """Detect influential observations using Cook's distance."""
    from statsmodels.stats.outliers_influence import OLSInfluence
    influence = OLSInfluence(model)
    cooks_d = influence.cooks_distance[0]
    return np.where(cooks_d > threshold)[0]


def pre_trends_test(model, pre_days=range(-14, -1)):
    """Test for pre-trends: joint F-test on pre-update days."""
    pre_vars = [f'day_{d}' for d in pre_days if f'day_{d}' in model.params.index]
    
    if not pre_vars:
        return None, None, None
    
    # Joint significance test
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    
    # Build restriction matrix
    r_matrix = np.zeros((len(pre_vars), len(model.params)))
    for i, var in enumerate(pre_vars):
        r_matrix[i, model.params.index.get_loc(var)] = 1
    
    # F-test under null that all pre-trend coefficients = 0
    wald_test = model.wald_test(r_matrix)
    return float(wald_test.statistic), float(wald_test.pvalue), pre_vars


def placebo_test(df, filtered_df, all_control_vars, placebo_day=-7, spec_name="Placebo"):
    """Placebo test: use fake update day, should get near-zero effect."""
    placebo_df = filtered_df.copy()
    placebo_df['days_from_placebo'] = placebo_df['days_from_update'] - placebo_df['days_from_update'].iloc[0] + placebo_day
    
    event_dummies = pd.get_dummies(placebo_df['days_from_placebo'], prefix='day')
    if 'day_-1' in event_dummies.columns:
        event_dummies = event_dummies.drop('day_-1', axis=1)
    elif 'day_-8' in event_dummies.columns:
        event_dummies = event_dummies.drop('day_-8', axis=1)
    
    for control in all_control_vars:
        if control in placebo_df.columns:
            event_dummies[control] = placebo_df[control]
    
    y = placebo_df['Players_scaled'].astype(float)
    X = sm.add_constant(event_dummies.astype(float))
    
    model = sm.OLS(y, X).fit()
    
    # Get coefficient for the "fake update day"
    placebo_coeff = None
    placebo_se = None
    for day in range(placebo_day - 2, placebo_day + 3):
        var_name = f'day_{day}'
        if var_name in model.params.index:
            placebo_coeff = model.params[var_name]
            placebo_se = model.bse[var_name]
            break
    
    results = {
        'spec': spec_name,
        'coeff_day0': placebo_coeff,
        'se_day0': placebo_se,
        'ci_low_day0': None,
        'ci_high_day0': None,
        'n_obs': int(model.nobs),
        'r_squared': model.rsquared,
        'model': model
    }
    
    return model, results


def create_robustness_table(results_list):
    """Create a formatted robustness check table."""
    data = []
    for res in results_list:
        row = {
            'Specification': res['spec'],
            'Day 0 Coeff': f"{res['coeff_day0']:.4f}" if res['coeff_day0'] is not None else "—",
            'Std. Error': f"({res['se_day0']:.4f})" if res['se_day0'] is not None else "—",
            '95% CI Low': f"{res['ci_low_day0']:.4f}" if res['ci_low_day0'] is not None else "—",
            '95% CI High': f"{res['ci_high_day0']:.4f}" if res['ci_high_day0'] is not None else "—",
            'N': res['n_obs'],
            'R²': f"{res['r_squared']:.3f}" if not np.isnan(res['r_squared']) else "—"
        }
        data.append(row)
    
    return pd.DataFrame(data)


def format_table_for_markdown(df):
    """Convert robustness table to markdown format."""
    return df.to_markdown(index=False)
