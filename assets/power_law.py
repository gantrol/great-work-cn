import numpy as np
import matplotlib.pyplot as plt

# Number of topics
N = 50

# Generate a list of topic indices
topics = np.array(range(1, N+1))

# Generate attention scores for each topic following a power law distribution
attention = 1.0 / np.power(topics, 2.0)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(topics, attention, marker='o')
plt.title('Attention Distribution Across Topics (Power Law)')
plt.xlabel('Topic')
plt.ylabel('Attention')
plt.grid(True)
plt.show()


# Adjust attention scores to percentages
attention_percentage = (attention / np.sum(attention)) * 100

# Select only the first 10 topics
topics_10 = topics[:10]
attention_percentage_10 = attention_percentage[:10]

# Plot
plt.figure(figsize=(8, 6))
plt.bar(topics_10, attention_percentage_10, alpha=0.75)
plt.title('Attention Distribution Across Topics (Power Law)')
plt.xlabel('Topic')
plt.ylabel('Attention (%)')
plt.xticks(topics_10)
plt.grid(True)
plt.show()
