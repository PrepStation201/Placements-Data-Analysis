import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import module

def main():
    module.print_title()
    #print_title()
    while True:
        print("\n\nChoose a category:")
        print("1. MTECH MDES")
        print("2. MSC MCA")
        print("q. Quit")

        category_choice = input("Enter your choice: ")

        if category_choice == 'q':
            break

        # Choose the appropriate data based on the user's category choice
        if category_choice == '1':
            data = module.read_csv_file('placement_data_pg.csv')
        elif category_choice == '2':
            data = module.read_csv_file('placement_data_pg_ms.csv')
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        while True:
            print("\nChoose a plotting function:")
            print("1. Bar Plot(Avg CTC Departmentwise in LPA):")
            print("2. Histogram(Min CTC in LPA vs No Of Counts)")
            print("3. Box Plot")
            print("4. Correlation Matrix")
            print("5. Line Plot")
            print("6. Pie Chart(Departmentwise Avg. CTC in %):")
            print("q. Back to category selection")

            plot_choice = input("Enter your choice: ")

            if plot_choice == 'q':
                break

            # Call the appropriate plotting function based on the user's choice
            if plot_choice == '1':
                module.bar_plot(data, 'Dept./Centre/School', 'Average CTC', 'Average CTC Across Departments')
            elif plot_choice == '2':
                module.histogram(data, 'Minimum CTC', 'Histogram of Minimum CTC')
            elif plot_choice == '3':
                module.box_plot(data, 'Dept./Centre/School', 'Median CTC', 'Median CTC Across Departments')
            elif plot_choice == '4':
                module.correlation_matrix(data[['Minimum CTC', 'Average CTC', 'Median CTC', 'Maximum CTC']], 'Correlation Matrix')
            elif plot_choice == '5':
                module.line_plot(data, 'Dept./Centre/School', 'Maximum CTC', 'Maximum CTC Across Departments')
            elif plot_choice == '6':
                module.pie_chart(data, 'Dept./Centre/School', 'Distribution of Departments')
            else:
                print("Invalid choice. Please enter a valid option.")

     # Define file paths
    excel_file_path1 = 'placement_data_pg.csv'
    excel_file_path2 = 'placement_data_pg_ms.csv'

    # Read CSV files into DataFrames
    data1 = module.read_csv_file(excel_file_path1)
    data2 = module.read_csv_file(excel_file_path2)

    # Compare datasets and create plots for pg and pg_msc
    module.compare_datasets([data1, data2], ["PG", "PG_MSc"])

    # Read CSV file
    file_path = 'compensation_details.csv'
    data_frame = module.read_csv_file(file_path)

    # Handle NaN values in 'Program' column
    data_frame['Program'] = data_frame['Program'].fillna('')

    # Convert numeric columns to numeric type
    numeric_cols = ['Minimum LPA-CTC', 'Average LPA-CTC', 'Median LPA-CTC', 'Maximum LPA-CTC (Domestic)', 'Maximum LPA-CTC (International)']
    data_frame[numeric_cols] = data_frame[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Split data into UG and PG DataFrames
    ug_df = data_frame[data_frame['Program'].str.contains('B.Tech|B.Des')]
    pg_df = data_frame[~data_frame['Program'].str.contains('B.Tech|B.Des')]

    # Plot the comparison
    module.plot_comparison(ug_df, pg_df)
    
if __name__ == "__main__":
    main()
