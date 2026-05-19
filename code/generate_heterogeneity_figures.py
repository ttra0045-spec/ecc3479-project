"""
Generate additional heterogeneity and comparative visualizations for the report.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Setup
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# Game classification
GAME_SPECS = [
    {"name": "Apex Legends", "file": "apex_legends_2025-01-28_to_2025-03-04.csv", "is_coop": False},
    {"name": "Counter Strike 2", "file": "counter_strike_2_2024-04-23_to_2024-05-28.csv", "is_coop": False},
    {"name": "Dead by Daylight", "file": "dead_by_daylight_2023-11-14_to_2023-12-19.csv", "is_coop": False},
    {"name": "Deep Rock Galactic", "file": "deep_rock_galactic_2024-05-30_to_2024-07-04.csv", "is_coop": True},
    {"name": "Destiny 2", "file": "destiny_2_2024-09-24_to_2024-10-29.csv", "is_coop": True},
    {"name": "Don't Starve Together", "file": "don_t_starve_together_2023-04-13_to_2023-05-18.csv", "is_coop": True},
    {"name": "Helldivers 2", "file": "helldivers_2_2025-08-19_to_2025-09-23.csv", "is_coop": True},
    {"name": "No Man's Sky", "file": "no_man_s_sky_2025-01-15_to_2025-02-19.csv", "is_coop": True},
    {"name": "Palworld", "file": "palworld_2024-12-09_to_2025-01-13.csv", "is_coop": True},
    {"name": "Path of Exile", "file": "path_of_exile_2025-06-06_to_2025-07-04.csv", "is_coop": True},
    {"name": "PUBG Battlegrounds", "file": "pubg__battlegrounds_2025-10-22_to_2025-11-26.csv", "is_coop": False},
    {"name": "Rainbow Six Siege", "file": "rainbow_six_siege_2024-08-19_to_2024-09-16.csv", "is_coop": False},
    {"name": "Sea of Thieves", "file": "sea_of_thieves_2024-10-03_to_2024-11-07.csv", "is_coop": True},
    {"name": "The Finals", "file": "the_finals_2024-12-05_to_2025-01-02.csv", "is_coop": False},
    {"name": "V Rising", "file": "v_rising_2025-04-21_to_2025-05-19.csv", "is_coop": True},
    {"name": "Warframe", "file": "warframe_2025-11-26_to_2025-12-31.csv", "is_coop": True},
]

# Load before-after changes data
before_after = pd.read_csv(output_dir / "before_after_changes.csv")

# Add game type classification
before_after['Game Type'] = before_after['Game'].apply(
    lambda x: 'Co-op' if next((g['is_coop'] for g in GAME_SPECS if g['name'] == x), False) else 'PvP'
)

# ============================================================================
# FIGURE 1: Game-Level Heterogeneity (Ranked Bar Chart)
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8), dpi=300)

# Sort by change magnitude
before_after_sorted = before_after.sort_values('Change', ascending=True)

# Create color mapping by game type
colors = ['#2E86AB' if game_type == 'Co-op' else '#A23B72' for game_type in before_after_sorted['Game Type']]

# Create bar chart
bars = ax.barh(range(len(before_after_sorted)), before_after_sorted['Change'], color=colors, edgecolor='black', linewidth=0.5)

# Customize
ax.set_yticks(range(len(before_after_sorted)))
ax.set_yticklabels(before_after_sorted['Game'], fontsize=10)
ax.set_xlabel('Before-After Change (z-score units)', fontsize=12, fontweight='bold')
ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_facecolor('#f8f9fa')

# Add value labels on bars
for i, (idx, row) in enumerate(before_after_sorted.iterrows()):
    value = row['Change']
    ax.text(value + 0.05, i, f'{value:.2f}', va='center', fontsize=9, fontweight='bold')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2E86AB', edgecolor='black', linewidth=0.5, label='Co-op'),
    Patch(facecolor='#A23B72', edgecolor='black', linewidth=0.5, label='PvP')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=11, framealpha=0.95)

plt.tight_layout()
fig.savefig(output_dir / 'Figure_5_Game_Level_Heterogeneity.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ heterogeneity_by_game_ranked.png")

# ============================================================================
# FIGURE 2: Co-op vs. PvP Event-Study Comparison
# ============================================================================

# Load event study coefficients
event_study = pd.read_csv(output_dir / "event_study_coefficients.csv")

# Create separate event studies for co-op and PvP games
# We need to recalculate by game type from raw data
data_clean_dir = Path("data:clean")

def load_and_process_by_type(game_specs, is_coop_filter):
    """Load and process data for a specific game type."""
    all_data = []
    
    for game in game_specs:
        if game['is_coop'] != is_coop_filter:
            continue
        
        df = pd.read_csv(data_clean_dir / game['file'])
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df['game'] = game['name']
        all_data.append(df)
    
    combined = pd.concat(all_data, ignore_index=True)
    
    # Standardize within each game
    standardized_frames = []
    for game_name in combined['game'].unique():
        game_df = combined[combined['game'] == game_name].copy()
        mean = game_df['Players'].mean()
        std = game_df['Players'].std()
        game_df['Players_scaled'] = (game_df['Players'] - mean) / std if std > 0 else 0
        standardized_frames.append(game_df)
    
    combined = pd.concat(standardized_frames, ignore_index=True)
    
    # Add day indicators
    combined['update_date'] = combined.groupby('game')['DateTime'].transform(lambda x: x.min())
    combined['day'] = (combined['DateTime'] - combined['update_date']).dt.days
    combined['day_cat'] = combined['day'].astype(int)
    
    return combined

coop_data = load_and_process_by_type(GAME_SPECS, True)
pvp_data = load_and_process_by_type(GAME_SPECS, False)

# Calculate mean and CI for each day
def calculate_by_day(data):
    """Calculate mean, SE, CI by day."""
    results = []
    for day in sorted(data['day_cat'].unique()):
        if day < -7 or day > 14:
            continue
        day_data = data[data['day_cat'] == day]['Players_scaled']
        if len(day_data) > 0:
            mean = day_data.mean()
            se = day_data.sem()
            ci_low = mean - 1.96 * se
            ci_high = mean + 1.96 * se
            results.append({'Day': day, 'Mean': mean, 'SE': se, 'CI_Low': ci_low, 'CI_High': ci_high})
    return pd.DataFrame(results)

coop_by_day = calculate_by_day(coop_data)
pvp_by_day = calculate_by_day(pvp_data)

# Plot comparison
fig, ax = plt.subplots(figsize=(14, 6), dpi=300)

# Plot both
ax.plot(coop_by_day['Day'], coop_by_day['Mean'], 'o-', color='#2E86AB', linewidth=2.5, markersize=7, label='Co-op games', zorder=3)
ax.fill_between(coop_by_day['Day'], coop_by_day['CI_Low'], coop_by_day['CI_High'], color='#2E86AB', alpha=0.2, zorder=1)

ax.plot(pvp_by_day['Day'], pvp_by_day['Mean'], 's-', color='#A23B72', linewidth=2.5, markersize=7, label='PvP games', zorder=3)
ax.fill_between(pvp_by_day['Day'], pvp_by_day['CI_Low'], pvp_by_day['CI_High'], color='#A23B72', alpha=0.2, zorder=1)

# Customize
ax.axvline(x=0, color='black', linestyle='--', linewidth=1.5, alpha=0.7, label='Update day')
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
ax.set_xlabel('Days relative to update', fontsize=12, fontweight='bold')
ax.set_ylabel('Effect on player engagement (z-score units)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_facecolor('#f8f9fa')
ax.legend(fontsize=11, loc='upper left', framealpha=0.95)
ax.set_xlim(-7.5, 14.5)

plt.tight_layout()
fig.savefig(output_dir / 'Figure_4_Heterogeneity_Coop_vs_PvP.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ heterogeneity_coop_vs_pvp_event_study.png")

# ============================================================================
# FIGURE 3: Correlation Analysis Heatmap
# ============================================================================

# Manually create correlation data based on the analysis
correlation_data = pd.DataFrame({
    'Game': [
        'Apex Legends',
        'Counter Strike 2',
        'Dead by Daylight',
        'Deep Rock Galactic',
        'Destiny 2',
        "Don't Starve Together",
        'Helldivers 2',
        "No Man's Sky",
        'Palworld',
        'Path of Exile',
        'PUBG Battlegrounds',
        'Rainbow Six Siege',
        'Sea of Thieves',
        'The Finals',
        'V Rising',
        'Warframe'
    ],
    'Correlation': [0.539019, 0.03115, 0.0269992, 0.560332, 0.409454, 0.597799, 
                    0.0600944, 0.771367, 0.785048, 0.645881, -0.0227268, 0.500692,
                    -0.14275, -0.122757, 0.763775, 0.530523]
})

# Add game type
correlation_data['Type'] = correlation_data['Game'].apply(
    lambda x: 'Co-op' if next((g['is_coop'] for g in GAME_SPECS if g['name'] in x), False) else 'PvP'
)

# Extract short game names for readability
correlation_data['Short_Name'] = correlation_data['Game'].str.split().str[0]

# Sort by correlation
correlation_data = correlation_data.sort_values('Correlation')

# Create visualization
fig, ax = plt.subplots(figsize=(12, 10), dpi=300)

# Color by correlation strength
colors_corr = plt.cm.RdBu_r((correlation_data['Correlation'] - correlation_data['Correlation'].min()) / 
                             (correlation_data['Correlation'].max() - correlation_data['Correlation'].min()))

bars = ax.barh(range(len(correlation_data)), correlation_data['Correlation'], color=colors_corr, edgecolor='black', linewidth=0.5)

ax.set_yticks(range(len(correlation_data)))
ax.set_yticklabels(correlation_data['Game'], fontsize=10)
ax.set_xlabel('Correlation: Day vs. Player Count (r)', fontsize=12, fontweight='bold')
ax.axvline(x=0, color='black', linestyle='-', linewidth=1.2)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_facecolor('#f8f9fa')

# Add value labels
for i, (idx, row) in enumerate(correlation_data.iterrows()):
    value = row['Correlation']
    ax.text(value + 0.02 if value > 0 else value - 0.02, i, f'{value:.3f}', 
            va='center', ha='left' if value > 0 else 'right', fontsize=9, fontweight='bold')

# Add trend interpretation lines
ax.axvline(x=0.3, color='green', linestyle=':', linewidth=1, alpha=0.5)
ax.axvline(x=-0.3, color='red', linestyle=':', linewidth=1, alpha=0.5)

# Add legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='red', linestyle=':', linewidth=1.5, label='Strong declining trend'),
    Line2D([0], [0], color='gray', linestyle='-', linewidth=1, label='No trend'),
    Line2D([0], [0], color='green', linestyle=':', linewidth=1.5, label='Strong growing trend'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10, framealpha=0.95)

plt.tight_layout()
fig.savefig(output_dir / 'Figure_1_Pre_existing_Trends.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ correlation_analysis_by_game.png")

print("\n" + "="*60)
print("All heterogeneity figures generated successfully!")
print("="*60)
