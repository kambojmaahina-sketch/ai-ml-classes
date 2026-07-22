import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("std_data.csv") 
print(df.head())

'''
plt.figure(figsize=(8, 5)) #chart code here 
plt.title("Chart Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.grid(True)
plt.show()
'''
'''
#--Line chart student marks
plt.figure(figsize=(8, 5))
plt.plot(
    df["Student name"],
    df["FinalMarks"],
    marker="o",
    color="green" )
plt.title("Student Final Marks")
plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
'''


#-- assignment-- line chart for Attendance by StudentName.
plt.figure(figsize=(8, 5))
plt.plot(
    df["Student name"],
    df["Attendance"],
    marker="o",
    color="green" )
plt.title("Student Attendance")
plt.xlabel("Student")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()