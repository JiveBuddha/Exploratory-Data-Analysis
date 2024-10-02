# exploratory_data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace this with your dataset)
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Display basic information about the dataset
print("Dataset Information:")
df.info()

# Display the first 5 rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())

# 1. Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 2. Missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 3. Univariate Analysis (Distribution of individual features)

# Distribution of Age
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'].dropna(), kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution.png')
plt.show()

# Distribution of Fare
plt.figure(figsize=(8, 6))
sns.histplot(df['Fare'], kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.savefig('fare_distribution.png')
plt.show()

# 4. Bivariate Analysis (Relationships between two variables)

# Relationship between Age and Survival
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Boxplot of Age by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.savefig('age_survival_boxplot.png')
plt.show()

# Relationship between Fare and Survival
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Boxplot of Fare by Survival')
plt.xlabel('Survived')
plt.ylabel('Fare')
plt.savefig('fare_survival_boxplot.png')
plt.show()

# 5. Categorical Variable Analysis (e.g., Gender and Survival)

# Countplot of Survival based on Sex
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Countplot of Survival by Gender')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.savefig('survival_by_gender.png')
plt.show()

# Countplot of Survival based on Embarked
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', hue='Embarked', data=df)
plt.title('Countplot of Survival by Embarked Location')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.savefig('survival_by_embarked.png')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

print("Exploratory Data Analysis complete. Visualizations saved as PNG files.")