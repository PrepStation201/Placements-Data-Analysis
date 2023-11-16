import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def print_title():
    text = "Placement Details 2022-2023"
    box_width = len(text) + 4
    print('*' * box_width)
    print(f'* {text} *')
    print('*' * box_width)
    
def read_csv_file(file_path):
    """
    Read the CSV file into a Pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data


def display_data_summary2(data, title):
    """
    Display the first few rows, information, and summary statistics of the DataFrame.
    """
    print(f"\n{title} Data Summary:")
    print("First few rows of the DataFrame:")
    print(data.head())
    print("\nDataFrame information:")
    print(data.info())
    print("\nDataFrame summary statistics:")
    print(data.describe())

def compare_datasets(data_list, titles):
    """
    Compare summary statistics and create bar plots for multiple datasets.
    """
    for data, title in zip(data_list, titles):
        display_data_summary2(data, title)

        # Select columns for comparison (you can customize these)
        comparison_columns = ['Minimum CTC', 'Average CTC', 'Median CTC', 'Maximum CTC']

        # Create bar plots for selected columns
        for column in comparison_columns:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Dept./Centre/School', y=column, data=data)
            plt.title(f'{title} - {column} Comparison')
            plt.show()

def plot_comparison(ug_df, pg_df):
    """
    Plot a side-by-side bar chart to compare UG and PG tables.
    """
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    # Plot UG Table
    ug_df.plot(kind='bar', ax=axes[0], title='UG Programs', rot=0, fontsize=10)
    axes[0].set_ylabel('LPA-CTC')
    axes[0].yaxis.tick_left()  # Move y-axis labels to the left

    # Plot PG Table
    pg_df.plot(kind='bar', ax=axes[1], title='PG Programs', rot=0, fontsize=10)
    axes[1].set_ylabel('LPA-CTC')
    axes[1].yaxis.tick_left()  # Move y-axis labels to the left

    plt.suptitle('Comparison of UG and PG Programs', y=1.02, fontsize=14)  # Adjust y parameter for suptitle
    plt.show()
def display_data_summary(data):
    
    print("First few rows of the DataFrame:")
    print(data.head())
    print("\nDataFrame information:")
    print(data.info())
    print("\nDataFrame summary statistics:")
    print(data.describe())


def bar_plot(data, x_col, y_col, title):
    """
    Create a bar plot to visualize the distribution of data across categories.
    """

    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_col, y=y_col, data=data)
    plt.title(title)
    plt.show()

def histogram(data, column, title):
    """
    Create a histogram to visualize the distribution of a numerical column.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=20, kde=True)
    plt.title(title)
    plt.show()

def box_plot(data, x_col, y_col, title):
    """
    Create a box plot to visualize the distribution of numerical data across categories.
    using matplotlib and seaborn
    """

    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_col, y=y_col, data=data)
    plt.title(title)
    plt.show()

def correlation_matrix(data, title):
    """
    Create a correlation matrix heatmap to visualize relationships between numerical variables.

    Parameters:
    - data: DataFrame containing the data.
    - title: Title for the plot.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.show()

def line_plot(data, x_col, y_col, title):
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_col, y=y_col, data=data, marker='o')
    plt.title(title)
    plt.show()

def pie_chart(data, column, title, value_col='Average CTC'):
    """
    Create a pie chart to visualize the distribution of average salaries across categories.
    """
    plt.figure(figsize=(8, 8))
    department_avg_salary = data.groupby(column)[value_col].mean()
    department_avg_salary.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.show()




