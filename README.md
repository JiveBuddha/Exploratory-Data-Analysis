# Exploratory Data Analysis (EDA) Project

## Project Overview

This project demonstrates an **Exploratory Data Analysis (EDA)** on a real-world dataset, specifically the Titanic dataset. EDA is a crucial step in any data analysis or data science project, helping to uncover patterns, spot anomalies, and test hypotheses. The goal of this project is to showcase how to extract meaningful insights from a dataset using various data visualization techniques.

Key steps performed in this project:
1. **Summary Statistics**: Understanding the basic statistical properties of the dataset.
2. **Missing Value Analysis**: Identifying and understanding missing data patterns.
3. **Univariate Analysis**: Analyzing individual features (distributions).
4. **Bivariate Analysis**: Exploring relationships between different variables.
5. **Categorical Variable Analysis**: Analyzing categorical features and their relationships with other variables.
6. **Correlation Heatmap**: Identifying the correlations between numerical features.

## Files in This Repository

- **exploratory_data_analysis.py**: This Python script performs the entire EDA workflow, including loading the dataset, visualizing data, and saving the plots.
- **age_distribution.png**: A visualization of the distribution of the Age feature.
- **fare_distribution.png**: A visualization of the distribution of the Fare feature.
- **age_survival_boxplot.png**: A boxplot showing the relationship between Age and Survival.
- **fare_survival_boxplot.png**: A boxplot showing the relationship between Fare and Survival.
- **survival_by_gender.png**: A count plot showing survival rates by gender.
- **survival_by_embarked.png**: A count plot showing survival rates by the port of embarkation.
- **correlation_heatmap.png**: A heatmap showing the correlation between numerical features.
- **README.md**: This file, which provides an overview of the project.

## How to Run the Project

1. **Install Required Libraries**:
   Ensure you have the following libraries installed:
   ```bash
   pip install pandas matplotlib seaborn