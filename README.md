# Week 4 Worksheet Repository: Exploratory Data Analysis

This repository is for the Timothy Tran's ECC3479

How do major game updates affect short-term player engagement trajectories?

## Repository Structure

Basic folder structure:

```text
ecc3479-project/
├── README.md                                         # Project overview, setup, and usage instructions.
├── requirements.txt                                  # Lists the Python packages needed to run the project.
├── Exploratory Data Analysis.md                      # A detailed report of the data analysis findings.
├── Code/                                             # Folder containing all Jupyter notebooks and scripts.
│   ├── Dataset manuplation from raw to clean.ipynb   # Notebook to process raw data into a clean, usable format.
│   ├── Trend Code.ipynb                              # Notebook for generating trend analysis plots.
│   ├── EDA.ipynb                                     # Notebook for initial exploratory data analysis.
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
   - [data:raw:](data:raw:): Original CSV files for 12 games (Palworld, Helldivers 2, No Man's Sky, Destiny 2, Counter-Strike 2, Apex Legends, Deep Rock Galactic, Don't Starve Together, Dead by Daylight, PUBG: BATTLEGROUNDS, Sea of Thieves, Warframe).
   - Raw rows contain timestamp and player-count values (DateTime and Players), stored in the original source format.

2. **Data cleaning and preparation**
   - [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb): Filters and prepares cleaned datasets, including metadata like update dates.
   - [data:clean:](data:clean:): Cleaned CSV files with standardized columns `DateTime,Players`.
   - Each clean file is date-filtered per game window, with the end date being 14 days after update date.
   - Each dataset is associated with an `update_date` tracking when the game received a major update or patch.

3. **Trend analysis and visualization**
   - [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb): Generates trend plots for all 12 games showing daily players, 7-day moving average, EMA smoothing, linear trend, and update date markers.
   - [outputs:](outputs:): Saved plot images (one per game) with filename pattern `game_name_players_trend.png`.
   - Each plot includes a red dotted vertical line marking the game's update date, helping visualize how major updates correlate with player count changes.

Additional files:
- [README.md](README.md): Project overview and instructions.
- [requirements.txt](requirements.txt): Python dependencies.

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

The [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb) notebook generates comprehensive trend plots for all 12 games. Each plot displays:

- **Daily Players** (blue line with markers): Raw daily player count data
- **7-Day Moving Average** (crimson line): Smoothed trend reducing daily noise
- **7-Day EMA** (purple line): Exponential moving average for responsive trend detection
- **Linear Trend** (dashed green line): Best-fit trend line across the entire period
- **Update Date** (red dotted vertical line): Marks when the game received a major update or patch

The update date line helps correlate player count changes with game updates. If you see a spike or dip in the moving averages near the update date, it indicates the update significantly affected player engagement.

All plots are saved to [outputs:](outputs:) with the naming pattern: `game_name_players_trend.png`

## Analysis Notes

Will be filled with analysis once it is done

## Documentation

- Raw data databook: [data:raw:/raw-data-databook.md](data:raw:/raw-data-databook.md)
- Clean data codebook: [data:clean:/clean-data-codebook.md](data:clean:/clean-data-codebook.md)


