import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/sanikaiyer/datathon/geo_cleaned.csv')

# Clean up column names (remove any leading/trailing spaces)
df.columns = df.columns.str.strip()

# Get a list of unique block groups
unique_block_groups = df['Block Group'].unique()

# Iterate over each unique block group
for block_group in unique_block_groups:
    # Filter data for the current block group
    block_group_data = df[df['Block Group'] == block_group]
    
    # Extract racial/ethnic percentages and convert them to floats
    racial_data = block_group_data[['% White', '% Asian', '% Black', '% Other', '% Two or More', '% American Indian', '% Pacific Islander']].replace('%', '', regex=True).astype(float).iloc[0]
    
    # Check if the data is non-zero to avoid empty charts
    if racial_data.sum() > 0:
        # Create a new figure for each pie chart to avoid overlapping
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Plot the pie chart without labels but with percentages
        wedges, _, autotexts = ax.pie(
            racial_data, 
            labels=None,  # No labels on the pie chart itself
            autopct='%1.1f%%',  # Show only percentages
            startangle=90, 
            pctdistance=0.8,  # Adjust distance of percentages from the center
            shadow=True, 
            wedgeprops={'edgecolor': 'black', 'linewidth': 1},
            textprops={'fontsize': 12}
        )
        
        # Set the title for the current block group
        ax.set_title(f'Racial/Ethnic Composition - {block_group}', fontsize=16, fontweight='bold')
        
        # Equal aspect ratio ensures the pie chart is circular
        ax.axis('equal')

        # Add a legend with racial/ethnic categories
        ax.legend(racial_data.index, loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=12, title='Categories')

        # Display the pie chart
        plt.tight_layout()
        plt.show()
        
        # Close the figure to free up memory and avoid overlap
        plt.close(fig)
