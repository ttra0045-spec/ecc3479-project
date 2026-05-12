# Week 4 Worksheet Repository: Exploratory Data Analysis

This repository is for Timothy Tran's ECC3479 project.

**Research Question**: How do major game updates affect short-term player engagement trajectories?

**Dataset**: Daily player count data for 16 multiplayer games over ~1-2 month periods, centered around major game updates.

**Analysis**: Event study design using OLS regression with control variables to estimate the causal effect of updates on player engagement.

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
│   ├── extra variables                               # File containing control variable specifications for each game.
│   ├── box plot code                                 # Script for creating box plots.
│   └── first_order_analysis.ipynb                    # Notebook for first-order and correlation analysis.
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
   - [Code/advanced_regression.ipynb](Code/advanced_regression.ipynb): Event study design measuring day-by-day effects of updates on player counts, with control variables for confounding events.
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

**What it does**: Estimates the causal effect of updates on player counts using an event study design with control variables.

### Step 6: Robustness Check Analysis

**Notebook**: [Code/robustness_checks.ipynb](Code/robustness_checks.ipynb)

1. Open the robustness checks notebook in VS Code
2. Run all cells
3. **Expected output**: Robustness summary table, placebo tests, pre-trends test, and interpretation

**What it does**: Stress-tests the main event-study estimate using alternative controls, alternative samples, robust inference methods, and placebo checks.

### Step 7: Review Final Analysis Report

**Document**: [analysis.md](analysis.md)

1. Open and read the comprehensive analysis report
2. Review tables, figures, and interpretation
3. Cross-reference with generated output files

---

## Verification Checklist

After running the pipeline, verify these files are present:

**Data files** (should be in [data:clean:](data:clean:)):
- [ ] palworld_2024-12-09_to_2025-01-13.csv
- [ ] warframe_2025-11-26_to_2025-12-31.csv
- [ ] counter_strike_2_2024-04-23_to_2024-05-28.csv
- [ ] (and 13 more game files)

**Output plots** (should be in [outputs:](outputs:)):
- [ ] dynamic_effects_plot.png (event study plot)
- [ ] combined_day_by_day_standardized_boxplot.png
- [ ] 16 individual game trend plots (palworld_players_trend.png, etc.)

**Output tables** (should be in [outputs:](outputs:)):
- [ ] event_study_table.html
- [ ] interaction_effects_table.html (if interaction model was run)
- [ ] robustness_summary_table.md

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
- **Control Variables**: Includes event indicators (holidays, sales, promotions, etc.) to isolate the update effect from other confounding factors.
- **Key Finding**: Updates lead to an average increase of **1.637 standard deviations** in player counts on the day of release (day 0), with effects persisting for several days.

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

## Documentation

- Raw data databook: [data:raw:/raw-data-databook.md](data:raw:/raw-data-databook.md)
- Clean data codebook: [data:clean:/clean-data-codebook.md](data:clean:/clean-data-codebook.md)
- Main analysis: [analysis.md](analysis.md)
- Robustness analysis: [Robustness_Check_Analysis.md](Robustness_Check_Analysis.md)


