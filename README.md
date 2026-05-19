# Game Update Player Engagement Report

**Research Question**: How do major game updates affect short-term player engagement?

**Dataset**: Daily Steam player count data for 16 multiplayer games over ~1-2 month periods, centered around major game updates.

**Methodology**: Event-study design using OLS regression with standardised within-game outcomes, HC3 robust standard errors, and clustered standard errors (by game).

**Main Finding**: Major updates generate an immediate engagement spike of **1.64 standard deviations** (95% CI: [1.12, 2.15]) on day 0, with effects persisting through day 14. Heterogeneity is substantial: co-op games respond more than PvP games.

---

## Quick Start: Reproduce All Results

```bash
# Install dependencies
pip install -r requirements.txt

# Generate all output tables and figures
python code/generate_report_tables.py
python code/generate_heterogeneity_figures.py

# All outputs saved to outputs/ folder
```

**For detailed reproducibility instructions, see [REPRODUCIBILITY.md](REPRODUCIBILITY.md)**

---

## Report Tables & Figures Mapping

The repo does not contain a `code/03_main_results.py` file. The equivalent production files are the scripts and notebooks below.

### Tables

| Report Location | Produced by | Output Files | Key Statistic |
|---|---|---|---|
| **Table 1: Sample Construction** | `code/generate_report_tables.py` | `Table_1_Summary_Statistics.csv/png` | 436 observations in ±14-day window |
| **Table 2: Event-Study Coefficients** | `code/generate_report_tables.py` | `Table_2_Event_Study_Coefficients.csv/png/html` | Day 0: **1.6367** ± 0.2617 |
| **Table 3: Before-After Changes** | `code/generate_report_tables.py` | `Table_3_Before_After_Changes.csv/png` | Pooled effect: **1.229** std devs |
| **Table 4: Robustness Checks** | `code/generate_report_tables.py` | `Table_4_Robustness_Checks.csv/png` | Coefficient stable across 12 specs |

### Figures

| Report Location | Produced by | Output File | Insight |
|---|---|---|---|
| **Figure 1: Pre-existing Trends** | `code/generate_heterogeneity_figures.py` | `Figure_1_Pre_existing_Trends.png` | Baseline momentum variation (r ranges from -0.14 to +0.79) |
| **Figure 2: Dynamic Effects** | `code/advanced_regression.ipynb` | `dynamic_effects_plot.png` | Coefficients peak day 3, fade by day 14 |
| **Figure 3: Distribution by Day** | `code/box plot code` | `combined_day_by_day_standardized_boxplot.png` | Median shifts up after day 0, variance remains high |
| **Figure 4: Co-op vs PvP** | `code/generate_heterogeneity_figures.py` | `Figure_4_Heterogeneity_Coop_vs_PvP.png` | Co-op: -1.0 on day 0; PvP: +0.3 (counter-intuitive) |
| **Figure 5: Game-Level Ranking** | `code/generate_heterogeneity_figures.py` | `Figure_5_Game_Level_Heterogeneity.png` | Range: V Rising +1.88 to Helldivers 2 -0.62 |

---

## Repository Structure

Basic folder structure:

```text
ecc3479-project/
├── README.md                                         # Project overview, setup, and usage instructions.
├── requirements.txt                                  # Lists the Python packages needed to run the project.
├── analysis.md                                       # Main analysis report with regression results and findings.
├── Exploratory Data Analysis.md                      # A detailed report of the data analysis findings.
├── Robustness_Check_Analysis.md                      # Robustness analysis report validating the main event-study result.
├── Code/                                             # Folder containing all Jupyter notebooks and scripts.
│   ├── Dataset manuplation from raw to clean.ipynb   # Notebook to process raw data into a clean, usable format.
│   ├── Trend Code.ipynb                              # Notebook for generating trend analysis plots.
│   ├── EDA.ipynb                                     # Notebook for initial exploratory data analysis.
│   ├── advanced_regression.ipynb                     # Event study and interaction analysis on update effects.
│   ├── robustness_checks.ipynb                       # Notebook for robustness checks on the event-study result.
│   ├── regression_analysis.ipynb                     # Regression models and statistical tests.
│   ├── first_order_analysis.ipynb                    # Notebook for first-order and correlation analysis.
│   ├── temp_analysis.ipynb                           # Temporary analysis notebook for exploratory work.
│   ├── generate_report_tables.py                     # Script to generate summary tables (CSV, PNG, HTML) for reports.
│   ├── generate_heterogeneity_figures.py             # Script to generate heterogeneity and comparative visualizations.
│   ├── robustness_utils.py                           # Utility functions for robustness checks and alternative specifications.
│   ├── verify_reproducibility.py                     # Verification script to check reproducibility of outputs.
│   ├── extra variables                               # File containing control variable specifications for each game.
│   └── box plot code                                 # Script/resource for creating box plots.
├── data:raw:/                                        # Folder for original, untouched data files.
│   ├── raw-data-databook.md                          # Data dictionary for the raw data.
│   └── *.csv                                         # The raw CSV data files for each game.
├── data:clean:/                                      # Folder for cleaned and preprocessed data.
│   ├── clean-data-codebook.md                        # Data dictionary for the cleaned data.
│   └── *.csv                                         # The cleaned CSV data files for each game.
├── outputs:/                                         # Folder for all generated outputs like charts and reports.
│   ├── *.png                                         # Image files of plots and charts.
│   ├── *.md                                          # Markdown reports summarizing analysis results.
│   └── *.csv                                         # CSV files with processed data or results.
└── src:/                                             # Folder for any Python source code modules (currently empty).
```

This repository is organized around a simple analysis pipeline:

1. **Raw data source**
   - [data:raw:](data:raw:): Original CSV files for 16 games (Palworld, Helldivers 2, No Man's Sky, Destiny 2, Counter-Strike 2, Apex Legends, Deep Rock Galactic, Don't Starve Together, Dead by Daylight, PUBG: BATTLEGROUNDS, Sea of Thieves, Warframe, Path of Exile, Rainbow Six Siege, The Finals, V Rising).
   - Raw rows contain timestamp and player-count values (DateTime and Players), stored in the original source format.

2. **Data cleaning and preparation**
   - [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb): Filters and prepares cleaned datasets, including metadata like update dates.
   - [data:clean:](data:clean:): Cleaned CSV files with standardized columns `DateTime,Players`.
   - Each clean file is date-filtered per game window, with the end date being 14 days after update date.
   - Each dataset is associated with an `update_date` tracking when the game received a major update or patch.

3. **Trend analysis and visualization**
   - [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb): Generates trend plots for all 16 games showing daily players, 7-day moving average, EMA smoothing, linear trend, and update date markers.
   - [outputs:](outputs:): Saved plot images (one per game) with filename pattern `game_name_players_trend.png`.
   - Each plot includes a red dotted vertical line marking the game's update date, helping visualize how major updates correlate with player count changes.

4. **Advanced regression analysis**
   - [Code/advanced_regression.ipynb](Code/advanced_regression.ipynb): Event study design measuring day-by-day effects of updates on player counts; overlap-event controls are tracked as labels in metadata.
   - [outputs/event_study_table.html](outputs/event_study_table.html): Full regression table from the event study model.
   - [outputs/dynamic_effects_plot.png](outputs/dynamic_effects_plot.png): Visualization of coefficient estimates and confidence intervals for each day relative to update.

Additional files:
- [README.md](README.md): Project overview and instructions.
- [requirements.txt](requirements.txt): Python dependencies.
- [analysis.md](analysis.md): Comprehensive analysis report including methodology, results, and interpretation.

## Running the Complete Analysis Pipeline

To reproduce all results from scratch, follow these steps **in order**:

### Step 1: Data Cleaning and Preparation

**Notebook**: [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb)

1. Open the notebook in VS Code
2. Select your Python kernel/environment
3. Run all cells (or just Cell 1 if it contains the full pipeline)
4. **Expected output**: Cleaned CSV files in [data:clean:](data:clean:) with naming pattern `game_name_startDate_to_endDate.csv`

**What it does**: Converts raw CSV files from [data:raw:](data:raw:) into analysis-ready format, filtering by date windows and adding update date metadata.

### Step 2: Exploratory Data Analysis

**Notebook**: [Code/EDA.ipynb](Code/EDA.ipynb)

1. Open the notebook in VS Code
2. Run all cells
3. **Expected output**: Summary statistics, distributions, and basic visualizations

**What it does**: Provides initial insights into the cleaned data structure and player count distributions across all 16 games.

### Step 3: Trend Analysis and Visualization

**Notebook**: [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb)

1. Open the notebook in VS Code
2. Run all cells
3. **Expected output**: Individual trend plots saved to [outputs:](outputs:) with pattern `game_name_players_trend.png`

**What it does**: Generates trend visualizations for all 16 games showing daily players, moving averages, and update date markers.

### Step 4: First-Order Analysis

**Notebook**: [Code/first_order_analysis.ipynb](Code/first_order_analysis.ipynb)

1. Open the notebook in VS Code
2. Run all cells
3. **Expected output**: Correlation analysis, summary statistics by game

**What it does**: Performs correlation and simple statistical tests on the data.

### Step 5: Advanced Regression Analysis (Event Study)

**Notebook**: [Code/advanced_regression.ipynb](Code/advanced_regression.ipynb)

1. Open the notebook in VS Code
2. **IMPORTANT**: Before running, ensure [Code/extra variables](Code/extra%20variables) file exists and contains the control variable specifications
3. Run all cells
4. **Expected output**: 
   - [outputs/dynamic_effects_plot.png](outputs/dynamic_effects_plot.png): Event study plot
   - [outputs/event_study_table.html](outputs/event_study_table.html): Full regression table

**What it does**: Estimates the causal effect of updates on player counts using an event study design; overlap-event controls are currently documented as labels rather than observed indicator columns.

### Step 6: Robustness Check Analysis

**Notebook**: [Code/robustness_checks.ipynb](Code/robustness_checks.ipynb)

1. Open the robustness checks notebook in VS Code
2. Run all cells
3. **Expected output**: Robustness summary table, placebo tests, pre-trends test, and interpretation

**What it does**: Stress-tests the main event-study estimate using alternative controls, alternative samples, robust inference methods, and placebo checks. Uses utility functions from [code/robustness_utils.py](code/robustness_utils.py).

### Step 7 (Optional): Generate Final Report Tables and Figures

All output files use standardized naming matching the Word document table/figure labels for reproducibility:

**Scripts**: 
- [Code/generate_report_tables.py](Code/generate_report_tables.py)
- [Code/generate_heterogeneity_figures.py](Code/generate_heterogeneity_figures.py)
- [Code/box plot code](Code/box%20plot%20code) - For Figure_3 distribution plot

Run these Python scripts to auto-generate final report tables and heterogeneity visualizations:

```bash
# Generate summary tables (CSV, PNG, HTML with standardized naming)
python code/generate_report_tables.py

# Generate heterogeneity analysis figures (Figure_1, Figure_4, Figure_5)
python code/generate_heterogeneity_figures.py

# Generate distribution plot (Figure_3)
python code/box\ plot\ code
```

**All expected outputs with standardized naming**:

**Tables:**
- `Table_1_Summary_Statistics.csv` / `.png` - Summary statistics by game
- `Table_2_Event_Study_Coefficients.csv` / `.png` / `.html` - Event-study coefficients and regression table
- `Table_3_Before_After_Changes.csv` / `.png` - Before-after changes by game
- `Table_4_Robustness_Checks.csv` / `.png` - Robustness checks for day-0 effect

**Figures:**
- `Figure_1_Pre_existing_Trends.png` - Pre-existing trends by game
- `Figure_2_Dynamic_Effects.png` - Dynamic effects around update day (generated by advanced_regression.ipynb)
- `Figure_3_Distribution_Standardised_Counts.png` - Distribution of standardised player counts
- `Figure_4_Heterogeneity_Coop_vs_PvP.png` - Co-op vs PvP comparison
- `Figure_5_Game_Level_Heterogeneity.png` - Game-level heterogeneity ranking

### Step 8: Review Final Analysis Report

**Document**: [analysis.md](analysis.md)

1. Open and read the comprehensive analysis report
2. Review tables, figures, and interpretation
3. Cross-reference with generated output files

### Reproducibility Verification (Optional)

To verify that all outputs have been successfully generated:

```bash
python code/verify_reproducibility.py
```

This will check that all required data files and outputs exist and validate key numerical results.

---

## Verification Checklist

After running the pipeline, verify these files are present (or run `python code/verify_reproducibility.py` for automated verification):

**Data files** (should be in [data:clean:](data:clean:)):
- [ ] palworld_2024-12-09_to_2025-01-13.csv
- [ ] warframe_2025-11-26_to_2025-12-31.csv
- [ ] counter_strike_2_2024-04-23_to_2024-05-28.csv
- [ ] (and 13 more game files)

**Output tables with standardized naming** (should be in [outputs:](outputs:)):
- [ ] Table_1_Summary_Statistics.csv and .png
- [ ] Table_2_Event_Study_Coefficients.csv, .png, and .html
- [ ] Table_3_Before_After_Changes.csv and .png
- [ ] Table_4_Robustness_Checks.csv and .png
- [ ] interaction_effects_table.html
- [ ] robustness_summary_table.md

**Output figures with standardized naming** (should be in [outputs:](outputs:)):
- [ ] Figure_1_Pre_existing_Trends.png
- [ ] Figure_2_Dynamic_Effects.png
- [ ] Figure_3_Distribution_Standardised_Counts.png
- [ ] Figure_4_Heterogeneity_Coop_vs_PvP.png
- [ ] Figure_5_Game_Level_Heterogeneity.png
- [ ] 16 individual game trend plots (palworld_players_trend.png, etc.)

**Main reports**:
- [ ] analysis.md (contains final results and interpretation)
- [ ] Robustness_Check_Analysis.md (contains the robustness checks and causal validation)

If all files are present, the pipeline has completed successfully and you should see results matching [analysis.md](analysis.md).


## Generate Clean Data From Raw Data

Use this notebook to convert raw files into analysis-ready clean files:

- [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb)

Steps:

1. Open [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb) in VS Code.
2. Select your Python kernel/environment.
3. Run Cell 1 (the full pipeline cell).
4. Check [data:clean:](data:clean:) for generated files named like:
   - `game_name_startDate_to_endDate.csv`

What this notebook does:

1. Reads source CSV files from [data:raw:](data:raw:).
2. Filters rows by each dataset's configured start/end window.
3. Associates each dataset with an `update_date` field (e.g., "2024-12-23" for Palworld) to track major game updates.
4. Writes clean CSV files to [data:clean:](data:clean:) with standardized columns `DateTime,Players`.
5. The metadata (including update dates) is used by the trend analysis notebook to mark update dates on plots.


## Trend Analysis & Visualization

The [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb) notebook generates comprehensive trend plots for all 16 games. Each plot displays:

- **Daily Players** (blue line with markers): Raw daily player count data
- **7-Day Moving Average** (crimson line): Smoothed trend reducing daily noise
- **7-Day EMA** (purple line): Exponential moving average for responsive trend detection
- **Linear Trend** (dashed green line): Best-fit trend line across the entire period
- **Update Date** (red dotted vertical line): Marks when the game received a major update or patch

The update date line helps correlate player count changes with game updates. If you see a spike or dip in the moving averages near the update date, it indicates the update significantly affected player engagement.

All plots are saved to [outputs:](outputs:) with the naming pattern: `game_name_players_trend.png`

## Advanced Regression Analysis

The [Code/advanced_regression.ipynb](Code/advanced_regression.ipynb) notebook implements an event study design to estimate the causal effect of game updates on player engagement:

- **Event Study Model**: Measures day-by-day changes in player counts for a 14-day window around each game update, with day -1 (before update) as the baseline.
- **Control Labels**: Tracks intended overlap events (holidays, sales, promotions, etc.) in metadata; cleaned files currently do not include those indicators as observed columns.
- **Key Finding**: Updates lead to an average increase of **1.64 standard deviations** in player counts on the day of release (day 0), with effects persisting for several days.

Results are documented in [analysis.md](analysis.md).

## Analysis Summary

The complete analysis is documented in [analysis.md](analysis.md), which includes:
- Descriptive statistics for all 16 games
- Before/after trend comparisons
- Event study regression results and interpretation
- Econometric specification and identification strategy
- Model equations and coefficient interpretation

## Output Files

Key outputs saved to [outputs:](outputs:):
- **Trend plots**: `[game_name]_players_trend.png` for all 16 games
- **Regression results**: `event_study_table.html`, `interaction_effects_table.html`
- **Robustness results**: `robustness_summary_table.md`, `robustness_results.json`
- **Visualizations**: `dynamic_effects_plot.png`, `combined_day_by_day_standardized_boxplot.png`
- **Analysis summaries**: Various `.md` files with analysis results

## Automated Report Generation Scripts

### generate_report_tables.py

This script automatically generates all summary tables used in the final report:

**Usage**:
```bash
python code/generate_report_tables.py
```

**What it does**:
- Loads cleaned data from all 16 games
- Generates summary statistics (sample sizes, player count ranges, update effects)
- Creates tables in multiple formats: CSV, PNG (as images), and HTML
- Outputs to `outputs/` folder

**Output files created**:
- `sample_construction.csv` - Sample sizes and date ranges per game
- `event_study_coefficients.csv` - Day-by-day coefficient estimates from event study
- `before_after_changes.csv` - Before-update vs after-update comparisons
- `summary_statistics.csv` - Descriptive statistics for each game

### generate_heterogeneity_figures.py

This script generates visualizations showing heterogeneous treatment effects across game types and individual games:

**Usage**:
```bash
python code/generate_heterogeneity_figures.py
```

**What it does**:
- Classifies games as Co-op vs PvP
- Creates comparative visualizations showing how different game types respond to updates
- Generates game-level heterogeneity rankings (which games see biggest effects)
- Produces bar charts and distributions of effects

**Key output files created**:
- `heterogeneity_coop_vs_pvp_event_study.png` - Comparison of Co-op vs PvP effects
- `heterogeneity_by_game_ranked.png` - Ranked bar chart of game-level effects
- Other heterogeneity analysis figures

### verify_reproducibility.py

Verification script to ensure all analysis outputs can be successfully regenerated:

**Usage**:
```bash
python code/verify_reproducibility.py
```

**What it does**:
- Checks that all 16 cleaned data files are present and valid
- Verifies that all required output files exist
- Validates key numerical results match expected values
- Provides a reproducibility checklist

**Output**: Console report showing which files pass/fail verification checks

## Utility Modules

### robustness_utils.py

Contains utility functions used by the robustness checks notebook for alternative specifications:

**Key functions**:
- `get_day_coefficient()` - Extracts coefficients and confidence intervals for specific event days
- `run_event_study()` - Runs event study models with alternative specifications
- Functions for outlier detection, inference robustness, and summary table generation
- Used primarily by [Code/robustness_checks.ipynb](Code/robustness_checks.ipynb)

## Additional Notebooks

The following notebooks are included in the code folder but are not part of the main analysis pipeline:

### regression_analysis.ipynb

Alternative or supplementary regression models and statistical tests. This notebook may contain experiments or alternative approaches to the main event study methodology.

### temp_analysis.ipynb

Temporary analysis notebook used for exploratory work and experimentation. This notebook is not part of the core reproducible pipeline.

## Standardized File Naming Convention

All output files follow a standardized naming convention matching the Word document table and figure labels. This ensures reproducibility and consistency across all generated outputs:

**Table Naming**: `Table_#_Description.{csv,png,html}`
- Example: `Table_1_Summary_Statistics.csv`

**Figure Naming**: `Figure_#_Description.png`
- Example: `Figure_1_Pre_existing_Trends.png`

This naming convention is enforced in all Python scripts and notebooks:
- [Code/generate_report_tables.py](Code/generate_report_tables.py) - Tables 1-4
- [Code/generate_heterogeneity_figures.py](Code/generate_heterogeneity_figures.py) - Figures 1, 4, 5
- [Code/advanced_regression.ipynb](Code/advanced_regression.ipynb) - Figure 2
- [Code/box plot code](Code/box%20plot%20code) - Figure 3

When you regenerate the outputs using any of the scripts, all files will automatically be named with these standard labels, making it easy to map them to the Word document.

## Documentation

- Raw data databook: [data:raw:/raw-data-databook.md](data:raw:/raw-data-databook.md)
- Clean data codebook: [data:clean:/clean-data-codebook.md](data:clean:/clean-data-codebook.md)
- Main analysis: [analysis.md](analysis.md)
- Robustness analysis: [Robustness_Check_Analysis.md](Robustness_Check_Analysis.md)


