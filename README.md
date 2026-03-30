# Week 4 Worksheet Repository: Exploratory Data Analysis

This repository is for the Timothy Tran's ECC3479

## Repository Structure

This repository is organized around a simple analysis pipeline:

1. **Raw data source**
   - [data:raw:](data:raw:): Original CSV files for 12 games (Palworld, Helldivers 2, No Man's Sky, Destiny 2, Counter-Strike 2, Apex Legends, Deep Rock Galactic, Don't Starve Together, Dead by Daylight, PUBG: BATTLEGROUNDS, Sea of Thieves, Warframe).
   - Raw rows contain timestamp and player-count values (DateTime and Players), stored in the original source format.

2. **Data cleaning and preparation**
   - [code/Dataset manuplation from raw to clean.ipynb](code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb): Filters and prepares cleaned datasets.
   - [data:clean:](data:clean:): Cleaned CSV files with standardized columns `DateTime,Players`.
   - Each clean file is date-filtered per game window, with the end date extended by 7 days (for example: `..._to_2025-03-04.csv`).

3. **Trend analysis and visualization**
   - [code/Trend Code.ipynb](code/Trend%20Code.ipynb): Generates trend plots (daily, moving average, EMA smoothing, linear trend).
   - [outputs:](outputs:): Saved plot images and analysis outputs.

Additional files:
- [README.md](README.md): Project overview and instructions.
- [requirements.txt](requirements.txt): Python dependencies.

## Getting Started

1. Create and activate a Python environment.
2. Install the required packages with `pip install -r requirements.txt`.
3. Open `code/Dataset manuplation from raw to clean.ipynb` in VS Code to make clean data.
4.Open `code/Trend Code.ipynb` In Vs code to make outputs about trends


## Analysis Notes

Will be filled with analysis once it is done

## Documentation

- Raw data databook: [data:raw:/raw-data-databook.md](data:raw:/raw-data-databook.md)


