import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('employee.csv')  # Ensure 'employee.csv' is in the same directory or specify the path

# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# 1. Calculate the average of the 'Salary' column
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: {average_salary}")

# 2. Find the maximum and minimum values in the 'Salary' column
max_salary = df['Salary'].max()
min_salary = df['Salary'].min()
print(f"\nMaximum Salary: {max_salary}")
print(f"Minimum Salary: {min_salary}")

# 3. Filter the DataFrame based on a condition (e.g., employees with Salary greater than 50000)
filtered_df = df[df['Salary'] > 50000]
print("\nEmployees with Salary greater than 50000:")
print(filtered_df)

# 4. Group data by 'Department' and calculate the average salary in each department
grouped_df = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(grouped_df)

# 5. Count the number of employees in each department
department_counts = df['Department'].value_counts()
print("\nNumber of Employees by Department:")
print(department_counts)

# 6. Calculate the total salary expenditure
total_salary = df['Salary'].sum()
print(f"\nTotal Salary Expenditure: {total_salary}")

# 7. Find the median salary of the employees
median_salary = df['Salary'].median()
print(f"\nMedian Salary: {median_salary}")

# 8. Identify the top 5 highest-paid employees
top_5_employees = df.nlargest(5, 'Salary')
print("\nTop 5 Highest-Paid Employees:")
print(top_5_employees)

# 9. Find the range of salaries (difference between max and min salary)
salary_range = max_salary - min_salary
print(f"\nSalary Range: {salary_range}")

# 10. Calculate the standard deviation of salaries
salary_std_dev = df['Salary'].std()
print(f"\nStandard Deviation of Salaries: {salary_std_dev}")

# 11. Group data by 'Department' and count employees within specified salary brackets
salary_bracket_counts = df.groupby('Department')['Salary'].apply(lambda x: pd.cut(x, bins=[0, 50000, 100000, 150000, float('inf')]).value_counts())
print("\nEmployee Count by Department and Salary Bracket:")
print(salary_bracket_counts)
