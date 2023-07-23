import matplotlib.pyplot as plt
import numpy as np

# Generate a range of trials from 0 to 120
trials = np.arange(0, 121, 1)

# Calculate the success probability for each number of trials
probabilities = 1 - (1 - p) ** trials

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(trials, probabilities, label='Success Probability')

# Highlight the point at 120 trials
plt.scatter([120], [0.7], color='red')
plt.text(121, 0.7, '70% success rate at 120 trials', verticalalignment='bottom')

# Add labels and title
plt.xlabel('Number of Trials')
plt.ylabel('Probability of At Least One Success')
plt.title('Probability of Success with Increasing Trials')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
