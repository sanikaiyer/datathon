import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your CSV file (adjust the path as needed)
df = pd.read_csv('/Users/sanikaiyer/datathon/requests_per_seat.csv', skiprows=2)

# Filter data for Webster Elementary School
webster_df = df[df['School Name'].str.contains('Webster', case=False, na=False)]

# Convert necessary columns to numeric (if not already)
webster_df[['Total Requests', 'Total Assigned', 'Total Seats']] = webster_df[['Total Requests', 'Total Assigned', 'Total Seats']].apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values (optional)
webster_df.dropna(subset=['Total Requests', 'Total Assigned', 'Total Seats'], inplace=True)

# Filter by grade (adjust column name if necessary)
# Assuming there is a 'Grade' column in the dataset
grades = ['K', '1', '2', '3', '4', '5']  # List the grades you want to include
filtered_df = webster_df[webster_df['Grade'].isin(grades)]

# Set up the data for the grouped bar chart
programs = filtered_df['Program Name']
total_requests = filtered_df['Total Requests']
total_assigned = filtered_df['Total Assigned']
total_seats = filtered_df['Total Seats']
grades_filtered = filtered_df['Grade']  # To label the x-ticks by grade

# Define the width of each bar and their positions
bar_width = 0.25
index = np.arange(len(programs))

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(index, total_requests, width=bar_width, label='Total Requests', color='skyblue')
plt.bar(index + bar_width, total_assigned, width=bar_width, label='Total Assigned', color='lightgreen')
plt.bar(index + 2 * bar_width, total_seats, width=bar_width, label='Total Seats', color='salmon')

# Add labels, title, and legend
plt.xlabel('Program Name (Filtered by Grade)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Program Comparison at Webster Elementary School', fontsize=14, fontweight='bold')
plt.xticks(index + bar_width, [f'{program} - {grade}' for program, grade in zip(programs, grades_filtered)], rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
