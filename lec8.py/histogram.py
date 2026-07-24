import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("std_data.csv")

# Histogram: marks distribution
plt.figure(figsize=(8,5))
plt.hist(
df["FinalMarks"],
bins=5,
color="blue",
edgecolor="black"
)
plt.title("Distribution of Final Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
#plt.savefig("student_marks_chart.png", dpi=300)    #saving chart as image
plt.show()