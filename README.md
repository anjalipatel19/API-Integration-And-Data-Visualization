# API-Integration-And-Data-Visualization

Python script that fetches asteroid data from NASA's API and visualizes near-Earth object counts and sizes using matplotlib.

**COMPANY:** CODETECH IT SOLUTIONS

**Name:** Anjali Dilip Patel

**INTERN ID:** CT06DL927

**Domain:** Python Programming

**BATCH Duration:** 6 Weeks

**Mentor:** Neela Santhosh Kumar

**PROJECT:** API INTEGRATION AND DATA VISUALIZATION

# NASA Asteroid Visualization Project

## Overview

This Python project fetches 7-day near-Earth asteroid data from NASA's NeoWs (Near Earth Object Web Service) API and generates professional visualizations displaying the number and average size of asteroids passing close to Earth during the selected date range.

## Features

* *API Integration*: Connects to NASA's NeoWs API to retrieve daily asteroid data
* *Data Processing*: Converts complex JSON responses into structured pandas DataFrames
* *Visualizations*:
  * Bar chart showing the number of near-Earth asteroids per day
  * Line chart illustrating average asteroid size (in kilometers) per day
* *Professional Styling*: Clear, clean layout with:
  * Date formatting on x-axis
  * Readable labels and titles
  * Balanced spacing and responsive layout

## Technical Details

* *Python Libraries Used*:
  * `requests` for API calls
  * `pandas` for data manipulation
  * `matplotlib` for plotting
* *Configuration*:
  * Easily update the time range via `START_DATE` and `END_DATE` variables
  * Replace the default `API_KEY` with your own from NASA
* *Output*:
  ![asteroid_report](https://github.com/user-attachments/assets/3e169860-8265-4066-95f0-ef18fc5a376e)

## Setup Instructions

1. Get your free NASA API key from [api.nasa.gov](https://api.nasa.gov/)
2. Replace the `API_KEY` in the script with your own key
3. Install required packages:

   ```bash
   pip install requests pandas matplotlib
   ```
4. Run the script:

   ```bash
   python nasa_asteroid_app.py
   ```

## Sample Output

The script creates and saves a dashboard (`asteroid_report.png`) with:

* Left panel: Bar chart of asteroid counts per day
* Right panel: Line chart of average asteroid diameter
* Formatted date labels and descriptive axes

## Customization

* Modify `START_DATE` and `END_DATE` to fetch different week ranges
* Swap the chart type or color scheme for custom visual preferences

## License

* *This project*: [MIT License](LICENSE) – Free to use, modify, and distribute
