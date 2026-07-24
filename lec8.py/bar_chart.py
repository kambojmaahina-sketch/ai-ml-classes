import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("std_data.csv") 


plt.figure(figsize=(8, 5))
plt.bar(
    df["Student name"],
    df["FinalMarks"],
    color="orange" )
plt.title("Student Final Marks")
plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.xticks(rotation=45)
#plt.savefig("student_marks_chart.png", dpi=300)    #saving chart as image
plt.show()


# Average marks by course as bar chart from groupby()
course_avg= df.groupby("Course")["FinalMarks"].mean()
plt.figure(figsize=(7, 5))
course_avg.plot(kind="bar", color="green")
plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.show()