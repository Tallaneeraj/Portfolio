# Analysis and Visualization of Global Renewable Energy Trends

## Overview
This repository contains a comprehensive analysis and visualization of global renewable energy trends. The study aims to understand the trends, challenges, and advancements in the adoption of renewable energy sources worldwide over the last 20 years.

## Contents
- **Introduction**
  - Overview of the global energy landscape and the need for renewable energy.
- **Dataset**
  - Detailed description of the dataset used, sourced from 'Our World in Data'.
- **Procedure**
  - Steps taken for data preprocessing, analysis, and visualization.
- **Results**
  - Key findings from the analysis, including major trends and regional differences in renewable energy adoption.
- **Conclusion**
  - Summary of insights gained and their implications for policy and decision-making.
- **Future Work**
  - Suggestions for further research to advance the understanding of global energy trends.

## Key Findings
1. **Global Trends**
   - Significant rise in renewable energy sources such as solar and wind.
   - Decrease in the share of fossil fuels in the global energy mix.
2. **Regional Insights**
   - Europe: Consistent reduction in greenhouse gas emissions, strong policy impacts.
   - Developing Countries: Mixed results with rapid economic expansion and urbanization challenges.
   - United States: Diverse energy portfolio with regional disparities in energy policy and resource utilization.

## Visualizations
- **Choropleth Maps**
  - Visual representation of renewable energy adoption across different regions.
- **Bar Charts**
  - Comparison of renewable vs. non-renewable energy sources.
- **Line Charts**
  - Trends in energy consumption and production over time.
- **Stacked Bar Charts**
  - Share of different energy sources in the global energy mix.


## Model Comparison: LSTM vs ARIMA
- To predict and compare energy consumption and electricity generation trends, both LSTM and ARIMA models were used. Here are the key findings:

- **Energy Consumption Predictions:**

   - ARIMA showed better stability and lower RMSE values compared to LSTM, particularly in countries like the United Kingdom, France, and Italy, where the data followed a predictable pattern.

   - LSTM struggled more with higher RMSE values, especially for the United States, which may have had complex, non-linear patterns that the LSTM model couldn't effectively capture without more extensive tuning and a larger dataset.

   - Key Insight: For stable, linear energy consumption patterns, ARIMA tends to be more reliable, whereas LSTM might need more data and tuning to capture complex trends.

- **Electricity Generation Predictions:**

  - ARIMA outperformed LSTM in terms of consistency and lower RMSE for most countries, especially where electricity generation data was less volatile (e.g., Germany, Italy, Spain).

  - The United States showed significant errors in both models due to its highly variable and complex electricity generation patterns.

  - Key Insight: ARIMA appears more suitable for linear trends in electricity generation, while LSTM might be more appropriate for non-linear, irregular datasets with more data points.

## How to Use
1. Clone the repository.
2. Open the Power BI file `Energy Data.pbix` to explore the detailed analysis.

## Contributing
If you have suggestions or improvements, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License.


## Data Source
The dataset used in this project is sourced from 'Our World in Data'. The data is used for demonstration purposes only, and all credits for the data go to the original creators.

Happy Analyzing! 📊🌍

