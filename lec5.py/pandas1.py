import pandas as pd
df=pd.read_csv('std_data.csv')   
print(df)
cols=['Student name','Course']

projected_df=df[['Student name','Course']]
print(projected_df)

high_scorers_df=df[df['FinalMarks']>=75]
print(high_scorers_df)

good_students_df=df[(df['FinalMarks']>=75) & (df['Attendance']>=80)]
print(good_students_df)

sorted_df=df.sort_values(by='FinalMarks', ascending=False)
print(sorted_df)
sorted_df.to_csv('sorted_std_data.csv', index=False)

pc=df.loc[1:3,['Student name','Course']]
print(pc)

selected_course_df=df[df['Course'].isin(['BCA','BCOM'])]
print(selected_course_df)

students_with_letter_a_df=df[df['Student name'].str.contains('y')]
print(students_with_letter_a_df)