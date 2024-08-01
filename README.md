# Data Stormers

## Description

My Project is a Python utility for interacting with various APIs. It includes functions for loading configuration files and making API requests. The project is designed to be modular and easy to extend.

## Features

- Load configuration from a JSON file
- Make API requests with different methods
- Example usage for weather, maps, and news APIs

## Prerequisites

- Python 3.6 or higher
- Required Python packages (listed in `requirements.txt`)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/DavidnBui/DataStormers.git
   cd DataStormers
   ```

2. **Set up your configuration file**

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