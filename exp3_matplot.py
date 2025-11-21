import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [50, 55, 65, 70, 80]
plt.scatter(x, y, label='Scores',
color='blue')
plt.plot(x, y, color='red', label='TrendLine')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Hours vs Test Score')
plt.grid(True)
plt.savefig('study_vs_score.png')
plt.figure()
plt.bar(x, y, color='green')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Bar Chart: Study Hours vsScore')
plt.show()
