
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('smoking.csv')

# Clean the data: convert numeric columns to appropriate types
df['age'] = df['age'].astype(int)
df['amt_weekends'] = pd.to_numeric(df['amt_weekends'], errors='coerce')
df['amt_weekdays'] = pd.to_numeric(df['amt_weekdays'], errors='coerce')

# Compute summary statistics
summary_stats = df.describe()

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(18, 20))

# Visualization 1: Age Distribution
sns.histplot(data=df, x='age', bins=10, kde=False, ax=axs[0, 0])
axs[0, 0].set_title('Age Distribution')
axs[0, 0].set_xlabel('Age')
axs[0, 0].set_ylabel('Frequency')

# Visualization 2: Smoking Status by Gender
sns.countplot(data=df, x='smoke', hue='gender', ax=axs[0, 1])
axs[0, 1].set_title('Smoking Status by Gender')
axs[0, 1].set_xlabel('Smoking Status')
axs[0, 1].set_ylabel('Count')

# Visualization 3: Gross Income Distribution
sns.countplot(data=df, x='gross_income', order=df['gross_income'].value_counts().index, ax=axs[1, 0])
axs[1, 0].set_title('Gross Income Distribution')
axs[1, 0].set_xlabel('Gross Income')
axs[1, 0].set_ylabel('Count')
for label in axs[1, 0].get_xticklabels():
    label.set_rotation(45)
    label.set_horizontalalignment('right')

# Visualization 4: Number of people smoking on weekends and weekdays
df_smoke = df[df['smoke'] == 'Yes']
smoking_counts = df_smoke[['amt_weekends', 'amt_weekdays']].count()
smoking_counts.index = ['Weekends', 'Weekdays']
smoking_counts.plot(kind='bar', ax=axs[1, 1])
axs[1, 1].set_title('Number of People Smoking on Weekends and Weekdays')
axs[1, 1].set_xlabel('Day Type')
axs[1, 1].set_ylabel('Number of People')

# Adjust layout to prevent overlap
plt.tight_layout()

# Add title and student information
fig.suptitle('Smoking and Demographic Data Visualisation\nStudent Name: Amulya Panithi\nStudent ID: 22089776', fontsize=16)
plt.subplots_adjust(top=0.88, bottom=0.15)

# Add explanations below the plots
fig.text(0.1, 0.05, 'Plot 1: The majority of individuals are between 30 and 50 years old.\n'
                    'Plot 2: More males do not smoke compared to females.\n'
                    'Plot 3: The largest income group earns between £5,200 to £10,400.\n'
                    'Plot 4: Smoking habits remain consistent on both weekends and weekdays.', 
         ha='left', fontsize=12)

# Save the infographic
plt.savefig('22089776.png', dpi=300)




