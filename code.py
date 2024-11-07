# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/mnt/data/heart.csv')

# Display basic information about the dataset
print("Dataset Shape:", data.shape)
print("\nFirst 5 rows of the dataset:")
print(data.head())
print("\nDataset Info:")
print(data.info())
print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Check the distribution of the target variable
print("\nTarget variable distribution (heart disease presence):")
print(data['target'].value_counts())
sns.countplot(x='target', data=data)
plt.title('Distribution of Heart Disease in Dataset')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.show()

# Check correlations between features
correlation_matrix = data.corr()
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Analyze the age distribution with heart disease
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', hue='target', multiple='stack', kde=True)
plt.title('Age Distribution by Heart Disease Status')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Analyze chest pain types with respect to heart disease
plt.figure(figsize=(10, 6))
sns.countplot(x='cp', hue='target', data=data)
plt.title('Chest Pain Type Distribution by Heart Disease Status')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.legend(title='Heart Disease')
plt.show()

# Analyze the effect of resting blood pressure (trestbps) on heart disease
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='trestbps', data=data)
plt.title('Resting Blood Pressure by Heart Disease Status')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Resting Blood Pressure')
plt.show()

# Check if cholesterol levels have any impact on heart disease
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='chol', data=data)
plt.title('Cholesterol Levels by Heart Disease Status')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Cholesterol')
plt.show()

# Analyze the maximum heart rate achieved by patients with and without heart disease
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='thalach', data=data)
plt.title('Max Heart Rate by Heart Disease Status')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Maximum Heart Rate')
plt.show()

# Check if fasting blood sugar > 120 mg/dl is related to heart disease
plt.figure(figsize=(6, 6))
sns.countplot(x='fbs', hue='target', data=data)
plt.title('Fasting Blood Sugar Distribution by Heart Disease Status')
plt.xlabel('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)')
plt.ylabel('Count')
plt.legend(title='Heart Disease')
plt.show()

# Analyze the effect of exercise induced angina on heart disease
plt.figure(figsize=(6, 6))
sns.countplot(x='exang', hue='target', data=data)
plt.title('Exercise Induced Angina by Heart Disease Status')
plt.xlabel('Exercise Induced Angina (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.legend(title='Heart Disease')
plt.show()

# Analyze the effect of ST depression induced by exercise on heart disease
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='oldpeak', data=data)
plt.title('ST Depression by Heart Disease Status')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('ST Depression (oldpeak)')
plt.show()
