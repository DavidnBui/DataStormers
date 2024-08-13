# DataStormers

## Description:
This project explores the impact of major storms, particularly tornadoes, on the U.S. housing market. By analyzing data from various sources, we aim to uncover trends in storm activity, disaster declarations, and the distribution of housing assistance funds. The project also examines how these factors affect housing prices and damage reports across different states. The visualizations created in this project help illustrate the geographic distribution of storm activity and its economic implications.

## Visualizations:
This project includes several key visualizations to illustrate the impact of storms on the housing market:
**Heatmap of Tornado Activity:** Highlights the geographic distribution of tornadoes across the U.S
**Tornado Frequency Bar Chart:** Shows the number of tornadoes by state.
**Trend of Disaster Declarations Over Time:** Displays the increase in disaster declarations over the years.
**Pie Chart - Distribution of Housing Assistance Funds:** Breaks down the types of housing assistance provided.
**Bar Chart - Total Housing Damage by State:** Illustrates the reported housing damage across states.
Each visualization was created using Python libraries such as Matplotlib, Seaborn, Folium, and Pandas.

## Analysis and Findings:
The analysis revealed several important findings:
**Increasing Disaster Declarations:** There is a clear upward trend in disaster declarations over time, indicating that storms are having a growing impact on communities.
**Geographic Concentration of Tornadoes:** Tornadoes are most frequent in Tornado Alley, affecting states like Oklahoma, Texas, and Kansas the most.
**Housing Assistance Distribution:** The majority of housing assistance funds are allocated to repair and replace housing, which is crucial for disaster recovery.
**State-Level Damage:** Ohio and Oklahoma report the highest total housing damage, suggesting that storm severity and housing density significantly influence the level of damage.

## Data Sources:
The project uses multiple datasets to conduct a thorough analysis:
**FEMA Disaster Declarations:** Contains data on federal disaster declarations, including the type of disaster, location, and date.
**NOAA Tornado Data:** Provides detailed information on tornado occurrences, including location, intensity, and damage reports.
**Housing Assistance Data:** Includes data on federal assistance provided for housing repairs, replacements, and other needs following a disaster.
**U.S. Census Data:** Offers demographic and economic data, such as median income, to contextualize the impact of storms on different communities.

## Project Structure:
The repository is organized as follows:
```bash
DataStormers/
│
├── data/                                     # Raw ###and processed data files
|     
├── testing/                                  # ##Jupyter notebooks for data indivdual notebooks
│     
├── utils/                                    # utilities needed for the program              
│
└── tornado_notebook.ipynb                    # main notebook of the project
└── data_dictionary.xlsx                      # layout of input files
└── data Stormers Presentaion                 # powerpoint of the project
└── config.template.json                      # json files for configurations
└── tornado_heatmap.html                      # ineractive heat_map graph
└── README.md                                 # Project README file
``` 

## Deployment

To deploy this project

1. **Clone the repository**

  ```bash
  git clone https://github.com/DavidnBui/DataStormers.git
  cd DataStormers
  ```

2. **Create a virtual environment**

  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. **Set up your configuration file**

  - Copy `config.template.json` to `config.json`:
  ```bash
  1. Copy `config.template.json` to `config.json`.
  2. Edit `config.json` and add your actual API keys and other credentials.
  3. Ensure `config.json` is not added to version control by checking that it's listed in `.gitignore`.
  ```

## Usage

To use the utilities in this project, you can run the `main.py` script or import functions from the `utils` package in your own scripts.

### Example Usage

Run the main script:

```bash
python main.py
```

This will fetch data using the API keys specified in `config.json`.

### Importing Functions

You can also use the functions directly in your own Python scripts:
```python
from utils import load_config, fetch_api_data

# Load configuration
config = load_config('config.json')

# Fetch data from an API
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Peoria"
params = {
    "unitGroup": "metric",
    "key": config.get('weather_api', {}).get('key'),
    "contentType": "json"
}
data = fetch_api_data(url, params=params)
print(data)
```

## Contributors

- Andrew (Data Visualization)
- Manahil (Data Visualization)
- Deelan (Data Analysis / Storytelling)
- Jeff (API Data)
- David (Data Cleaning)