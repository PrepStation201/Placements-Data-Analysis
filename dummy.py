import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'],
        'Score': [80, 85, 90, 75, 95]}

student_data = pd.DataFrame(data)
student_data['Date'] = pd.to_datetime(student_data['Date'])  # Convert 'Date' to datetime

# Line plot
plt.figure(figsize=(10, 6))
plt.plot(student_data['Date'], student_data['Score'], marker='o', linestyle='-')
plt.title('Student Performance Over Time')
plt.xlabel('Date')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# Insights
insights = "\nUseful Insights:\n"
insights += "1. Overall Trend:\n   - The student scores show a positive overall trend, increasing over time.\n"
insights += "2. Peaks and Valleys:\n   - Peak at May 2022 suggests a significant improvement in performance.\n"
insights += "   - Valley at April 2022 indicates a dip in scores that might need attention.\n"
insights += "3. Outliers:\n   - No obvious outliers observed; scores seem relatively stable without extreme variations.\n"
insights += "4. Patterns or Seasonality:\n   - No clear recurring patterns or seasonality observed in the data.\n"
insights += "5. Correlation with Events:\n   - Further investigation is needed to determine if specific events correlate with score changes.\n"

# Print or use the insights as needed
print(insights)

# You can now use the 'insights' variable for further processing or display.
