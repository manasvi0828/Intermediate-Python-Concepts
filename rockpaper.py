import matplotlib.pyplot as plt

# Sample array
data = [10, 20, 30, 40, 50]

# X-axis labels
labels = ['A', 'B', 'C', 'D', 'E']

# Plotting the bar graph
plt.bar(labels, data)

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Example')

# Displaying the plot
plt.show()
