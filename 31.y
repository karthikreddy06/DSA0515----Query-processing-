import numpy as np
import matplotlib.pyplot as plt
means_men = np.array([22, 30, 35, 35, 26])
means_women = np.array([25, 32, 30, 35, 29])
std_men = np.array([4, 3, 4, 1, 5])
std_women = np.array([3, 5, 2, 3, 3])
categories = ['A', 'B', 'C', 'D', 'E']
x = np.arange(len(categories))
width = 0.5
fig, ax = plt.subplots(figsize=(8, 6))
bar1 = ax.bar(x, means_men, width, label='Men', color='skyblue', yerr=std_men, capsize=5)
bar2 = ax.bar(x, means_women, width, label='Women', color='lightcoral', bottom=means_men, yerr=std_women, capsize=5)
ax.set_xlabel('Categories')
ax.set_ylabel('Scores')
ax.set_title('Stacked Bar Plot with Error Bars')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.tight_layout()
plt.show()
