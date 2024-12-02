import matplotlib.pyplot as plt
data = [55, 65, 70, 90, 80, 55, 60, 75, 85,
        90, 72, 88, 91, 76, 59, 67, 73, 89, 94, 78]
plt.hist(data, bins=5, edgecolor='black')
plt.title("Distribution of Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()
