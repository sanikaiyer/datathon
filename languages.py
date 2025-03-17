import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sanikaiyer/datathon/CLEANED_SHAREABLE_Application_Request_Data.csv')

schools_to_include = ['Webster (Daniel) ES']
filtered_df = df[df['SchoolName'].isin(schools_to_include)]

#print(filtered_df)

x = df['Language Spoken by Student at Home']
selected_values = ['Spanish', 'Cantonese', 'Mandarin (Putonghua)']
filt_df = df[df['Language Spoken by Student at Home'].isin(selected_values)]
#filt_df = df[~df['Language Spoken by Student at Home'].isin(['English'])]
counts = filt_df['Language Spoken by Student at Home'].value_counts()
filtered_counts = counts[counts >= 20]


plt.figure(figsize=(10, 6))
filtered_counts.plot(kind='bar')

plt.xlabel('Language Spoken by Student at Home')
plt.ylabel('Count')
plt.title('Distribution of Languages Spoken by Students')
plt.tight_layout()       

plt.show()



