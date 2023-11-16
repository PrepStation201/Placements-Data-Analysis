import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv_file(file_path):
    """
    Read the CSV file into a Pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data

def display_data_summary(data, title):
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
        display_data_summary(data, title)

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

def main():
    # Define file paths
    excel_file_path1 = 'placement_data_pg.csv'
    excel_file_path2 = 'placement_data_pg_ms.csv'

    # Read CSV files into DataFrames
    data1 = read_csv_file(excel_file_path1)
    data2 = read_csv_file(excel_file_path2)

    # Compare datasets and create plots
    compare_datasets([data1, data2], ["PG", "PG_MSc"])

    # Read CSV file
    file_path = 'compensation_details.csv'
    data_frame = read_csv_file(file_path)

    # Handle NaN values in 'Program' column
    data_frame['Program'] = data_frame['Program'].fillna('')

    # Convert numeric columns to numeric type
    numeric_cols = ['Minimum LPA-CTC', 'Average LPA-CTC', 'Median LPA-CTC', 'Maximum LPA-CTC (Domestic)', 'Maximum LPA-CTC (International)']
    data_frame[numeric_cols] = data_frame[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Split data into UG and PG DataFrames
    ug_df = data_frame[data_frame['Program'].str.contains('B.Tech|B.Des')]
    pg_df = data_frame[~data_frame['Program'].str.contains('B.Tech|B.Des')]

    # Plot the comparison
    plot_comparison(ug_df, pg_df)

if __name__ == "__main__":
    main()
