# Heart Disease Exploratory Data Analysis

This project performs an Exploratory Data Analysis (EDA) on a heart disease dataset to uncover insights about key factors associated with heart disease. The analysis focuses on understanding relationships between patient attributes and the presence of heart disease, providing insights to support healthcare strategies for prevention and treatment.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Overview](#dataset-overview)
- [EDA Steps](#eda-steps)
- [Visualizations](#visualizations)
- [Installation and Setup](#installation-and-setup)


## Project Overview

Heart disease is a leading cause of mortality worldwide. This project aims to leverage data analysis techniques to examine factors influencing heart disease presence. By analyzing demographic, lifestyle, and medical data, this project seeks to reveal hidden patterns and correlations, potentially guiding medical interventions and lifestyle recommendations.

## Dataset Overview

The dataset contains patient data including age, sex, cholesterol levels, blood pressure, chest pain types, and other key indicators. The target variable indicates the presence of heart disease (1 = heart disease, 0 = no heart disease).

Key variables include:
- `age`: Age of the patient
- `sex`: Gender of the patient
- `cp`: Chest pain type (e.g., typical angina, atypical angina, non-anginal pain, asymptomatic)
- `trestbps`: Resting blood pressure
- `chol`: Serum cholesterol in mg/dl
- `thalach`: Maximum heart rate achieved
- `fbs`: Fasting blood sugar > 120 mg/dl
- `target`: Presence of heart disease (1 = disease, 0 = no disease)

## EDA Steps

1. **Data Loading and Cleaning**: Import the data, examine the structure, and handle any missing values.
2. **Descriptive Statistics**: Generate summary statistics to understand the data distribution.
3. **Target Variable Analysis**: Analyze the distribution of heart disease cases.
4. **Feature Correlation**: Examine correlations between features and with the target variable to identify significant associations.
5. **Feature-specific Analysis**:
   - Age distribution by heart disease status
   - Chest pain types and their relation to heart disease
   - Impact of cholesterol levels, blood pressure, and heart rate on heart disease
   - Relationship between fasting blood sugar, exercise-induced angina, and heart disease

## Visualizations

The following visualizations are generated in this project:
- **Target Variable Distribution**: Bar chart showing patients with and without heart disease.
- **Correlation Matrix**: Heatmap to visualize correlations among features.
- **Age Distribution**: Histogram split by heart disease status.
- **Chest Pain Analysis**: Count plot for chest pain types, split by heart disease status.
- **Blood Pressure, Cholesterol, and Heart Rate**: Boxplots showing distributions by heart disease status.
- **Fasting Blood Sugar and Exercise-induced Angina**: Count plots for these factors based on heart disease presence.

## Installation and Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/heart-disease-eda.git
