import matplotlib.pyplot as plt

# Sample data for Internet users by continent (in millions)
continents = [
    'Asia', 'Europe', 'North America', 'Africa', 'South America', 'Oceania'
]
internet_users = [2500, 700, 320, 500, 260,
                  30]  # Corresponding users in millions

# Create a bar chart
plt.figure(figsize=(12, 6))  # Set the figure size

# Plotting the data
bars = plt.bar(
    continents,
    internet_users,
    color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
    alpha=0.7)

# Adding the title and labels
plt.title('Growth of Internet Users by Continent',
          fontsize=16)  # Title of the plot
plt.xlabel('Continents', fontsize=14)  # X-axis label
plt.ylabel('Number of Internet Users (in millions)',
           fontsize=14)  # Y-axis label

# Adding the data labels on top of the bars
for bar in bars:
  yval = bar.get_height()  # Get the height of the bar to place the label
  plt.text(bar.get_x() + bar.get_width() / 2,
           yval,
           int(yval),
           va='bottom',
           ha='center',
           fontsize=11)

# Adding a legend (if necessary, for this case the legend is somewhat redundant)
plt.legend(['Internet Users'], loc='upper right', fontsize=12)

# Show the grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot with tight layout
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot
