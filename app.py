#Import libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for Shiny
ui.page_opts(title="PyShiny App with Plot", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # A a slider for the specifying nunber of bins in the histogram
    # The ui.input_slider function is called with five arguments:
    # A string id ("selected_number_of_bins") that uniquely identifies this input value. 
    # A string label ("Number of Bins") to be displayed alongside the slider.
    # An integer representing the minimum number of bins (0).
    # An integer representing the maximum number of bins (100).
    # An integer representing the initial value of the slider (20).
    # A string id ("selected_number_of_bins") that uniquely identifies this input value. 
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

# Define a plot function for rendering a histogram 
@render.plot(alt="Histogram showing the distribution")
def histogram():
    # Define the number of points to generate
    count_of_points: int = 100
    # Set a random seed for reproducibility
    np.random.seed(3)
    # Generate random data for histogram
    random_data_array = 100 + 15 * np.random.random(count_of_points)
    # Create a histogram of the random data using plt.hist()
    x = 100 + 15 * np.random.randn(100)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color='black')
    plt.title('Histogram showing the distribution')

# Define a plot function for rendering the heatmap
@render.plot(alt="Heatmap showing the distribution")
def heatmap():
    # Define the number of points to generate
    count_of_points: int = 100
    # Set a random seed for reproducibility
    np.random.seed(3)
    # Generate random data array
    random_data_array_x = 100 + 15 * np.random.random(count_of_points)
    random_data_array_y = 100 + 15 * np.random.random(count_of_points)
    # Create a 2D histogram of the random data using the selected number of bins
    plt.hist2d(random_data_array_x, random_data_array_y, bins=input.selected_number_of_bins(), density=True, cmap='coolwarm')
    # Add labels and title
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Heatmap showing the distribution')
