from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load your dataset (make sure to provide the correct path)
data = pd.read_csv('E:\\College\\5th Semester\\Data Analysis\\SDG_Year.csv')

# Define your plotting function
def plot_sdg_comparison(country1, country2, sdg):
    # Filter the data for the specified countries and SDG
    filtered_data = data[(data['Country Name'].isin([country1, country2])) &
                        (data['SDG'] == sdg)]
    
    # Check if there is any data for the specified countries and SDG
    if filtered_data.empty:
        return None  # No data available
    
    # Pivot the data to get years as rows and countries as columns
    pivoted_data = filtered_data.pivot_table(index='Year', columns='Country Name', values='Value')
    
    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(pivoted_data.index, pivoted_data[country1], marker='o', label=country1)
    plt.plot(pivoted_data.index, pivoted_data[country2], marker='o', label=country2)
    
    plt.title(f'Time Series Comparison of {country1} and {country2} for {sdg}')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the figure to free up memory
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()  # Return image as base64

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    country1 = request.form['country1']
    country2 = request.form['country2']
    unsdg = request.form['unsdg']

    # Call the plot function and get the plot URL
    plot_url = plot_sdg_comparison(country1, country2, unsdg)

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
