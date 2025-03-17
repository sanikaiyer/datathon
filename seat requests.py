import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load your CSV file (adjust the path as needed)
df = pd.read_csv('/path/to/Requests per Seat Data.csv', skiprows=2)

# Filter data for Webster Elementary School
webster_df = df[df['School Name'].str.contains('Webster', case=False, na=False)]

# Convert necessary columns to numeric (if not already)
webster_df[['Total Requests', 'Total Assigned', 'Total Seats']] = webster_df[['Total Requests', 'Total Assigned', 'Total Seats']].apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values (optional)
webster_df.dropna(subset=['Total Requests', 'Total Assigned', 'Total Seats'], inplace=True)

# Set up the data for the grouped bar chart
programs = webster_df['Program Name']
grades = webster_df['Grade']
total_requests = webster_df['Total Requests']
total_assigned = webster_df['Total Assigned']
total_seats = webster_df['Total Seats']

# Melt the DataFrame for easier plotting with Seaborn
melted_df = webster_df.melt(id_vars=['Program Name', 'Grade'], 
                            value_vars=['Total Requests', 'Total Assigned', 'Total Seats'], 
                            var_name='Metric', value_name='Count')

# Create a grouped bar chart using Seaborn
plt.figure(figsize=(12, 8))
sns.barplot(data=melted_df, 
            x='Program Name', y='Count', 
            hue='Metric', 
            palette=['skyblue', 'lightgreen', 'salmon'],
            ci=None)

# Add annotations for Grade on each bar
for i, row in melted_df.iterrows():
    plt.text(i // 3, row['Count'] + 0.5, f"Grade {row['Grade']}", ha='center', fontsize=8)

# Add labels, title, and legend
plt.xlabel('Program Name', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Program Comparison by Grade at Webster Elementary School', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Metric')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
