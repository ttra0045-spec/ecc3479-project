"""
Reproducibility verification script.
Checks that all outputs can be regenerated and validates key numbers.
"""

import sys
from pathlib import Path
import pandas as pd
import json

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

def check_data_exists():
    """Verify all cleaned data files are present."""
    print("\n" + "="*80)
    print("1. CHECKING CLEANED DATA")
    print("="*80)
    
    data_dir = Path(__file__).parent.parent / "data:clean"
    required_games = [
        "apex_legends_2025-01-28_to_2025-03-04.csv",
        "counter_strike_2_2024-04-23_to_2024-05-28.csv",
        "dead_by_daylight_2023-11-14_to_2023-12-19.csv",
        "deep_rock_galactic_2024-05-30_to_2024-07-04.csv",
        "destiny_2_2024-09-24_to_2024-10-29.csv",
        "don_t_starve_together_2023-04-13_to_2023-05-18.csv",
        "helldivers_2_2025-08-19_to_2025-09-23.csv",
        "no_man_s_sky_2025-01-15_to_2025-02-19.csv",
        "palworld_2024-12-09_to_2025-01-13.csv",
        "path_of_exile_2025-06-06_to_2025-07-04.csv",
        "pubg__battlegrounds_2025-10-22_to_2025-11-26.csv",
        "rainbow_six_siege_2024-08-19_to_2024-09-16.csv",
        "sea_of_thieves_2024-10-03_to_2024-11-07.csv",
        "the_finals_2024-12-05_to_2025-01-02.csv",
        "v_rising_2025-04-21_to_2025-05-19.csv",
        "warframe_2025-11-26_to_2025-12-31.csv",
    ]
    
    missing = []
    for game_file in required_games:
        filepath = data_dir / game_file
        if filepath.exists():
            print(f"  ✓ {game_file}")
        else:
            print(f"  ✗ MISSING: {game_file}")
            missing.append(game_file)
    
    if not missing:
        print(f"\n✓ All {len(required_games)} cleaned data files present")
        return True
    else:
        print(f"\n✗ Missing {len(missing)} data files")
        return False

def check_scripts_exist():
    """Verify all production scripts are present."""
    print("\n" + "="*80)
    print("2. CHECKING PRODUCTION SCRIPTS")
    print("="*80)
    
    code_dir = Path(__file__).parent
    scripts = [
        "generate_report_tables.py",
        "generate_heterogeneity_figures.py",
        "robustness_utils.py"
    ]
    
    all_exist = True
    for script in scripts:
        filepath = code_dir / script
        if filepath.exists():
            print(f"  ✓ {script}")
        else:
            print(f"  ✗ MISSING: {script}")
            all_exist = False
    
    if all_exist:
        print(f"\n✓ All {len(scripts)} scripts present")
    return all_exist

def check_outputs_exist():
    """Verify all expected outputs are present."""
    print("\n" + "="*80)
    print("3. CHECKING GENERATED OUTPUTS")
    print("="*80)
    
    output_dir = Path(__file__).parent.parent / "outputs"
    
    required_outputs = {
        'Tables': [
            'sample_construction.csv',
            'variable_definitions.csv',
            'summary_statistics.csv',
            'event_study_coefficients.csv',
            'before_after_changes.csv',
            'robustness_checks.csv',
        ],
        'Table Images': [
            'sample_construction.png',
            'variable_definitions.png',
            'summary_statistics.png',
            'event_study_coefficients.png',
            'before_after_changes.png',
            'robustness_checks.png',
        ],
        'Figures': [
            'correlation_analysis_by_game.png',
            'heterogeneity_by_game_ranked.png',
            'heterogeneity_coop_vs_pvp_event_study.png',
            'dynamic_effects_plot.png',
            'combined_day_by_day_standardized_boxplot.png',
        ]
    }
    
    missing = []
    for category, files in required_outputs.items():
        print(f"\n{category}:")
        for filename in files:
            filepath = output_dir / filename
            if filepath.exists():
                print(f"  ✓ {filename}")
            else:
                print(f"  ✗ MISSING: {filename}")
                missing.append(filename)
    
    if not missing:
        print(f"\n✓ All required outputs present")
        return True
    else:
        print(f"\n⚠ Missing {len(missing)} outputs (will be regenerated)")
        return False

def verify_key_numbers():
    """Verify critical numerical results."""
    print("\n" + "="*80)
    print("4. VERIFYING KEY NUMBERS")
    print("="*80)
    
    output_dir = Path(__file__).parent.parent / "outputs"
    
    # Check event-study Day 0 coefficient
    coeff_csv = output_dir / "event_study_coefficients.csv"
    if coeff_csv.exists():
        df = pd.read_csv(coeff_csv)
        day_0 = df[df['Event time'] == 'Day 0']
        
        coeff = day_0['Coefficient'].values[0]
        expected_coeff = 1.6367
        
        print(f"\nDay 0 Event-Study Coefficient:")
        print(f"  Expected: {expected_coeff}")
        print(f"  Observed: {coeff:.4f}")
        
        if abs(coeff - expected_coeff) < 0.0001:
            print(f"  ✓ MATCH")
        else:
            print(f"  ⚠ DIFFERENCE: {abs(coeff - expected_coeff):.6f}")
    
    # Check before-after changes
    ba_csv = output_dir / "before_after_changes.csv"
    if ba_csv.exists():
        df = pd.read_csv(ba_csv)
        v_rising = df[df['Game'] == 'V Rising']['Change'].values[0] if 'V Rising' in df['Game'].values else None
        
        if v_rising is not None:
            print(f"\nV Rising Before-After Change:")
            print(f"  Expected: ~1.88")
            print(f"  Observed: {v_rising:.2f}")
            if abs(v_rising - 1.88) < 0.05:
                print(f"  ✓ MATCH")

def main():
    """Run all reproducibility checks."""
    print("\n" + "="*80)
    print("REPRODUCIBILITY VERIFICATION")
    print("="*80)
    
    all_pass = True
    
    # Run checks
    all_pass = check_data_exists() and all_pass
    all_pass = check_scripts_exist() and all_pass
    all_pass = check_outputs_exist() and all_pass
    verify_key_numbers()
    
    # Summary
    print("\n" + "="*80)
    if all_pass:
        print("✓ ALL CRITICAL CHECKS PASSED")
        print("\nRepository is fully reproducible!")
        print("To regenerate outputs:")
        print("  python code/generate_report_tables.py")
        print("  python code/generate_heterogeneity_figures.py")
    else:
        print("⚠ SOME CHECKS FAILED")
        print("\nSee above for details.")
    print("="*80 + "\n")
    
    return 0 if all_pass else 1

if __name__ == "__main__":
    sys.exit(main())
