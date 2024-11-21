import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)  
x = np.random.rand(100)  
y = np.random.rand(100)  
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('X-axis (Random Distribution)')
plt.ylabel('Y-axis (Random Distribution)')
plt.title('Scatter Plot of Randomly Distributed Data')
plt.tight_layout()
plt.show()
