import pandas as pd

df=pd.read_csv('std_data.csv')

print(df.head())

print(f"Number of students {len(df)}")

print("Rows and Columns:")
print(df.shape)

print("Average Marks:")
print(df["FinalMarks"].mean())

print("Average Attendance:")
print(df["Attendance"].mean())

#-- Count Categories With value_counts(),
print("Count pass and fail students")
print(df["Result"].value_counts())

print("Count male and female students")
print(df["Gender"].value_counts())

print("Count students by course")
print(df["Course"].value_counts())

#-- Percentage Distribution
print("Percentage of Pass and Fail students")
result_percent = df["Result"].value_counts(
    normalize=True
) * 100
print(result_percent)

#-- Average Marks By Course
print("Average marks by course")
course_avg = df.groupby("Course")["FinalMarks"].mean()
print(course_avg)

#-- Multiple Calculations With agg()
print("Course-wise summary report")
course_summary = df.groupby("Course")["FinalMarks"].agg([
    "count",
    "mean",
    "max",
    "min"
])
print(course_summary)

#-- Multiple Columns In Summary
print("Analyze marks and attendance together")
summary = df.groupby("Course").agg({
    "FinalMarks": ["mean", "max", "min"],
    "Attendance": ["mean", "min"],
    "Student ID": "count"
})

print(summary)

#-- Grouping by 2 columns
print("Course and Result wise count")
course_result = df.groupby([
    "Course",
    "Result"
])["Student ID"].count()

print(course_result)

#-- Make group output cleaner
print("Groupby result into normal table")
course_result = df.groupby([
    "Course",
    "Result"
])["Student ID"].count().reset_index()
print(course_result)

#-- Pivot table
print("Pivot table: Course vs Result")
pivot = pd.pivot_table(
    df,
    values="Student ID",
    index="Course",
    columns="Result",
    aggfunc="count",
    fill_value=0
)
print(pivot)

#-- Find top performing course
print("Course with highest average marks")
course_avg = df.groupby("Course")["FinalMarks"].mean()

top_course = course_avg.idxmax()
top_average = course_avg.max()

print("Top Course:", top_course)
print("Average Marks:", top_average)

#-- Pass percentage by course
print("Create pass percentage by course")
pass_data = df[df["Result"] == "Pass"]
total_by_course = df.groupby("Course")["Student ID"].count()
pass_by_course = pass_data.groupby("Course")["Student ID"].count()
pass_percent = (pass_by_course / total_by_course) * 100
print(pass_percent)