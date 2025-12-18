# plt.scatter(x, y, color = 'color_name', marker = 'marker_style', label = 'label_name')

import matplotlib.pyplot as plt

hours_studies = [1,2,3,4,5,6,7,8]
exam_scores = [50,55,60,65,70,75,80,85]

# scatter plot
# marker = 'o' matlab circle hota hai.
plt.scatter(hours_studies, exam_scores, color='green', marker='o', label='Student Data')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Releation Between Study and time and Exam Score")
plt.legend()
plt.grid(True)
plt.show()

