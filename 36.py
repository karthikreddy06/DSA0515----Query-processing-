import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42) 
group1_weights = np.random.normal(60, 5, 30)  
group1_heights = np.random.normal(160, 10, 30) 
group2_weights = np.random.normal(70, 6, 30)  
group2_heights = np.random.normal(170, 8, 30)  
group3_weights = np.random.normal(80, 7, 30) 
group3_heights = np.random.normal(180, 6, 30)  
plt.figure(figsize=(10, 7))
plt.scatter(group1_weights, group1_heights, color='blue', alpha=0.7, label='Group 1', edgecolor='black')
plt.scatter(group2_weights, group2_heights, color='green', alpha=0.7, label='Group 2', edgecolor='black')
plt.scatter(group3_weights, group3_heights, color='red', alpha=0.7, label='Group 3', edgecolor='black')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Scatter Plot Comparing Weights and Heights for Three Groups')
plt.legend(title='Groups')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.tight_layout()
plt.show()
