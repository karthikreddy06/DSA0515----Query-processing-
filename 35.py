import matplotlib.pyplot as plt
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.figure(figsize=(8, 6))
plt.scatter(math_marks, science_marks, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot: Mathematics vs Science Marks')
plt.xticks(marks_range)
plt.yticks(marks_range)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
