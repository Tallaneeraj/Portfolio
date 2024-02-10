
## DinoFunWorld Amusement Park Data Analysis

This repository contains a comprehensive analysis of one day's worth of operations at the DinoFunWorld Amusement Park. The analysis utilizes a provided SQLite database containing information about visitor check-ins, attractions, and visitor sequences throughout the park.

### Overview

The analysis aims to provide insights into various aspects of park operations, including popular attractions, ride visit times, attendance at food stalls, visitor paths, ride attendance dynamics, and the performance of specific attractions such as the newest ride, Atmosfear.

### Analysis Highlights

1. **Popular Attractions**: Determined the most popular attraction in the park based on visitor check-ins.

2. **Longest Visit Time**: Identified the ride with the longest average visit duration.

3. **Fast Food Offering**: Determined the fast food offering with the fewest visitors.

4. **Skyline of Visits and Visit Time**: Computed the skyline of the number of visits and visit time for park rides, highlighting prominent rides.

5. **Thrill Ride Visits**: Presented a pie chart depicting visits to thrill ride attractions.

6. **Total Visits to Food Stalls**: Illustrated total visits to food stalls with a bar chart.

7. **Attendance at Atmosfear**: Analyzed attendance trends at the newest ride, Atmosfear, over the course of the day using a line chart.

8. **Total Visits to Kiddie Rides**: Presented total visits to the park's kiddie rides using a box-and-whisker plot.

9. **Visitor Paths Analysis**: Constructed a distance matrix for a sample of visitors to understand their paths through the park.

10. **Ride Attendance Dynamics**: Examined minimum, average, and maximum attendance at each ride using a parallel coordinate plot and scatterplot matrix.

11. **Atmosfear Attendance Control Chart**: Created a control chart displaying attendance, mean, and standard deviation bands to address concerns about attendance fluctuations.

12. **Moving Average Chart**: Provided a moving average chart of Atmosfear attendance to further analyze attendance trends.

13. **Exponentially-weighted Moving Average**: Presented an exponentially-weighted moving average of Atmosfear attendance for additional analysis.

14. **Visitor Trajectory Dendrogram**: Generated a dendrogram graph using visitor trajectories to visualize visitor similarities based on their paths through the park.

### Repository Structure

- **Code**: Contains Jupyter Notebook files with Python code for data analysis and visualization.
- **Data**: Includes the SQLite database file ('dinofunworld.db') provided by the park administration.
- **README.md**: Provides an overview of the analysis, instructions for accessing the data, and a summary of the analysis results.

### How to Use

1. Clone the repository to your local machine.
2. Install the necessary dependencies (e.g., Python, Jupyter Notebook, SQLite3).
3. Open and run the Jupyter Notebook files in the 'Code' directory to reproduce the analysis and visualize the results.
4. Explore the findings and insights provided in each notebook to gain a comprehensive understanding of DinoFunWorld Amusement Park's operations.
