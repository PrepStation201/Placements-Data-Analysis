import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def read_excel_file(file_path):
    """
    Read the Excel file into a Pandas DataFrame.
    """
    data = pd.read_excel(file_path)
    return data

def display_data_summary(data):
    """
    Display the first few rows, information, and summary statistics of the DataFrame.
    """
    print("First few rows of the DataFrame:")
    print(data.head())
    print("\nDataFrame information:")
    print(data.info())
    print("\nDataFrame summary statistics:")
    print(data.describe())

def plot_gender_distribution(data):
    """
    Plot the distribution of gender in the dataset.
    """
    gender_distribution = data['gender'].value_counts()
    gender_distribution.plot(kind='bar', color=['skyblue', 'lightcoral'])
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

def plot_average_package_by_branch(data):
    """
    Plot the average package for each branch.
    """
    average_package_by_branch = data.groupby('Branch')['salary'].mean().sort_values()
    average_package_by_branch.plot(kind='barh', color='green')
    plt.title('Average Package by Branch')
    plt.xlabel('Average Package (in LPA)')
    plt.ylabel('Branch')
    plt.show()

def plot_cgpa_vs_package(data):
    """
    Plot the relationship between CGPA and Package.
    """
    plt.scatter(data['cpi'], data['salary'], alpha=0.5, color='orange')
    plt.title('CGPA vs Package')
    plt.xlabel('CGPA')
    plt.ylabel('Package (in LPA)')
    plt.show()

def plot_top_companies(data, top_n=15):
    """
    Plot a bar chart for the distribution of the top N companies recruiting students.
    """
    total_students = len(data)
    top_companies = data['company'].value_counts().nlargest(top_n)

    # Calculate the percentage of students recruited by each company
    top_companies_percentage = (top_companies / total_students) * 100

    # Create a DataFrame for the top companies and their percentage
    top_companies_data = pd.DataFrame({'Company': top_companies_percentage.index, 'Percentage': top_companies_percentage.values})

    # Plot the bar chart with percentage scale
    plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
    sns.barplot(x='Percentage', y='Company', data=top_companies_data, palette='viridis')
    plt.title(f'Top {top_n} Companies Recruiting Students (Percentage Scale)')
    plt.xlabel('Percentage of Students Recruited')
    plt.ylabel('Company')
    plt.show()

def convert_salary_to_numeric(data):
    """
    Convert 'salary' column to numeric (removing commas).
    """
    data['salary'] = data['salary'].replace({',': ''}, regex=True).astype(float)

def plot_salary_distribution_by_branch(data):
    """
    Create a violin plot for the distribution of salaries by branch.
    """
    plt.figure(figsize=(12, 8))
    sns.violinplot(x='Branch', y='salary', data=data, palette='viridis')
    plt.title('Distribution of Salaries by Branch')
    plt.xlabel('Branch')
    plt.ylabel('Salary (in LPA)')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.show()

def main():
    excel_file_path = 'placements2022.xlsx'
    data = read_excel_file(excel_file_path)

    # Task 1: Display data summary
    display_data_summary(data)

    # Task 2: Plot gender distribution
    plot_gender_distribution(data)

    # Task 3: Plot average package by branch
    plot_average_package_by_branch(data)

    # Task 4: Plot CGPA vs Package
    plot_cgpa_vs_package(data)

    # Task 5: Plot company distribution
    plot_top_companies(data, top_n=15)

    # Task 6: Convert 'salary' column to numeric
    convert_salary_to_numeric(data)

    # Task 7: Plot salary distribution by branch
    plot_salary_distribution_by_branch(data)

if __name__ == "__main__":
    main()
