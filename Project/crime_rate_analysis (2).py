# -*- coding: utf-8 -*-
"""crime_rate_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fo0JVym-HkpQW5GhnquAucwj4SnsLO14
"""

from google.colab import files
uploaded = files.upload()



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("crime_rate_dataset.csv")
df.head()

df.isna().sum()

df.describe()

plt.style.use('seaborn-v0_8-darkgrid')
sns.set(rc={'figure.figsize': (14, 8)})

total_crimes_by_year = df.groupby('YEAR')['TOTAL IPC CRIMES'].sum()

plt.figure(figsize=(12, 6))
sns.barplot(x=total_crimes_by_year.index, y=total_crimes_by_year.values, color='darkred')
plt.title("Total IPC Crimes in India (Year-wise)")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_states = df.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='Reds_r')
plt.title("Top 10 States/UTs by Total IPC Crimes (All Years)")
plt.xlabel("Total IPC Crimes")
plt.ylabel("State/UT")
plt.tight_layout()
plt.show()

key_crimes = ['MURDER', 'RAPE', 'THEFT']
crime_trends = df.groupby('YEAR')[key_crimes].sum()

plt.figure(figsize=(14, 7))
for crime in key_crimes:
    plt.plot(crime_trends.index, crime_trends[crime], marker='o', label=crime)

plt.title("Trends of Major Crimes in India Over the Years")
plt.xlabel("Year")
plt.ylabel("Reported Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

women_crimes = [
    'RAPE',
    'ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY',
    'CRUELTY BY HUSBAND OR HIS RELATIVES'
]
latest_year = df['YEAR'].max()
latest_data = df[df['YEAR'] == latest_year]
women_data_latest = latest_data[women_crimes].sum()

plt.figure(figsize=(12, 12))  # Increased from (8, 8) to (12, 12)
plt.pie(
    women_data_latest,
    labels=women_crimes,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
    textprops={'fontsize': 14}  # Optional: make labels larger
)
plt.title(f"Crimes Against Women Distribution – {latest_year}", fontsize=18)
plt.axis('equal')  # Ensures the pie is circular
plt.tight_layout()
plt.show()

crime_columns = ['MURDER', 'RAPE', 'KIDNAPPING & ABDUCTION', 'THEFT', 'RIOTS', 'CHEATING', 'DOWRY DEATHS']
heatmap_data = latest_data.set_index('STATE/UT')[crime_columns]

plt.figure(figsize=(16, 10))
sns.heatmap(heatmap_data, cmap='Reds', annot=True, fmt="d", linewidths=0.5)
plt.title(f"Crime Distribution by State – {latest_year}")
plt.xlabel("Crime Type")
plt.ylabel("State/UT")
plt.tight_layout()
plt.show()

