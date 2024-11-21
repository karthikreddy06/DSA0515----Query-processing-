import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)  
x = np.random.rand(100) 
y = np.random.rand(100) 
sizes = np.random.rand(100) * 1000  
plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, s=sizes, color='blue', alpha=0.5, edgecolor='black')
plt.xlabel('X-axis (Random Distribution)')
plt.ylabel('Y-axis (Random Distribution)')
plt.title('Scatter Plot with Randomly Sized Balls')
plt.tight_layout()
plt.show()
