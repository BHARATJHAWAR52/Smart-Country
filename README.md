# Smart Country - SDG Comparator

**Smart Country** is a web application designed to compare the progress of different countries based on various indicators related to the United Nations Sustainable Development Goals (SDGs). This tool provides a visual comparison of time series data for selected SDGs between two countries.

## Features
- Compare two countries based on SDG indicators.
- Visualize time series data to track progress across years.
- Custom weightings of indicators to align rankings with UN SDG rankings.
- Support for multiple SDG categories like Sustainability, Quality of Life, Economic Development, and more.

## Getting Started

### Prerequisites
To run the app, ensure you have the following installed:
- Python 3.x
- Required libraries listed in `requirements.txt`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BHARATJHAWAR52/Smart-Country.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Smart-Country/my_sdg_comparator
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Once the dependencies are installed, you can run the app locally:

```bash
python app.py
```

This will start the web application on `http://127.0.0.1:5000`. Open this link in your browser to start using the SDG comparator.

## Project Structure

- **app.py**: The main Flask application file.
- **/static**: Contains static assets like CSS, JavaScript files.
- **/templates**: Contains HTML templates for the frontend.
- **requirements.txt**: List of Python dependencies required to run the app.
- **my_sdg_comparator/**: Contains the main logic for comparing countries based on SDG indicators.

## Usage

### Key Functionality
- **SDG Comparison**: Select two countries and one SDG from the list, and the application will generate a time series plot comparing their performance based on selected indicators.
  
- **Indicator Weighting**: The application aggregates multiple indicators for each SDG, applying custom-defined weights to calculate scores for each country. It also normalizes the data to ensure comparability across different scales.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Contributions are welcome to expand the dataset, improve visualizations, or add new features.

---
