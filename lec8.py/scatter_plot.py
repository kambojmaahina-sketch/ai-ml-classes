import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("std_data.csv")

# scatter plot Study Hours vs FinalMarks
# plt.figure(figsize=(8,5))
plt.scatter(
    df["StudyHours"],
    df["FinalMarks"],
    color="orange",
)
plt.title("Study Hours vs FinalMarks")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
#plt.savefig("student_marks_chart.png", dpi=300)    #saving chart as image
plt.show()