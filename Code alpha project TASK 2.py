# ✅ TASK 2: Exploratory Data Analysis (EDA) 
# ● Ask meaningful questions about the dataset before analysis. 
# ● Explore the data structure, including variables and data types. 
# ● Identify trends, patterns and anomalies within the data. 
# ● Test hypotheses and validate assumptions using statistics and visualization. 
# ● Detect potential data issues or problems to address in further analysis. 

# Step 1: Ask Meaningful Questions
# Before analyzing, here are some guiding questions:
# - Q1: Does smoking status significantly affect insurance price?
# - Q2: Is there a correlation between BMI and insurance price?
# - Q3: Do males and females pay different insurance premiums on average?
# - Q4: How does the number of children influence insurance cost?
# - Q5: Are there any outliers or anomalies in BMI or insurance price?

# Explore Data Structur

import pandas as pd

# Load the Excel file
df = pd.read_excel("C:\\Users\\DELL\\Desktop\\Healthcare-Insurance-Sample-Data 2.xlsx")

# Basic structure
print(df)
print(df.info())
print(df.describe(include='all'))

#Code for Visual Exploration

import seaborn as sns
import matplotlib.pyplot as plt

# Distribution of insurance price
sns.histplot(df['Insurance Price (USD)'], kde=True)
plt.title("Distribution of Insurance Price")
plt.show()

# Boxplot by Smoking Status
sns.boxplot(x='Smoking Status', y='Insurance Price (USD)', data=df)
plt.title("Insurance Price by Smoking Status")
plt.show()

# Scatterplot: BMI vs Insurance Price
sns.scatterplot(x='BMI', y='Insurance Price (USD)', hue='Smoking Status', data=df)
plt.title("BMI vs Insurance Price")
plt.show()

# Boxplot by Gender
sns.boxplot(x='Gender', y='Insurance Price (USD)', data=df)
plt.title("Insurance Price by Gender")
plt.show()

# Code for Statistical Tests

from scipy.stats import ttest_ind, pearsonr

# Q1: Smoking vs Non-Smoking
smokers = df[df['Smoking Status'] == 'Smoker']['Insurance Price (USD)']
non_smokers = df[df['Smoking Status'] == 'Non-Smoker']['Insurance Price (USD)']
t_stat, p_val = ttest_ind(smokers, non_smokers)
print(f"Smoking vs Non-Smoking t-test: t={t_stat:.2f}, p={p_val:.4f}")

# Q2: Correlation between BMI and Insurance Price
corr, p_corr = pearsonr(df['BMI'], df['Insurance Price (USD)'])
print(f"BMI vs Insurance Price correlation: r={corr:.2f}, p={p_corr:.4f}")

# Q3: Gender-based price difference
male = df[df['Gender'] == 'Male']['Insurance Price (USD)']
female = df[df['Gender'] == 'Female']['Insurance Price (USD)']
t_gender, p_gender = ttest_ind(male, female)
print(f"Male vs Female t-test: t={t_gender:.2f}, p={p_gender:.4f}")

# Code to Check Anomalies

# Check for outliers in BMI and Insurance Price
sns.boxplot(data=df[['BMI', 'Insurance Price (USD)']])
plt.title("Outlier Detection")
plt.show()

# Check for duplicate names
print("Duplicate Names:", df['Name'].duplicated().sum())

# Check for extreme BMI values
print("BMI > 40:", df[df['BMI'] > 40])

