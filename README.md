# Heart Disease Prediction (AI/ML Project)

## Dataset
- Cardiovascular dataset (70,000 entries)

## Phases
- Phase 1: Data Collection
- Phase 2: EDA & Data Processing
- Phase 3: Data Training & Integration

## Project Overview
The Cardio Prediction Project is an end-to-end machine learning system designed to predict the presence of cardiovascular disease in patients based on clinical health metrics. By leveraging a structured data pipeline, the project encompasses data cleaning, feature engineering, and the training of multiple classification models-including Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Machines (SVM)-to provide accurate health risk assessments.

# Phase 1: Data Collection
Data Source: [Kaggle]

Dataset Size: 70,000 rows, 13 features.

# Phase 2: EDA & Processing
Cleaning:
- Removed id
- Converted age to years
- Handled nulls using median imputation

Key Insights: 
- Cleaning: The dataset was prepared by removing the irrelevant id column, scaling the age feature to years for better interpretability, and applying median imputation to ensure data completeness.

- Heatmap Insights: The correlation heatmap demonstrates that age, cholesterol, and weight exhibit the strongest positive correlations with the presence of cardiovascular disease, while other features show weaker individual linear relationships. The data distribution is well-balanced across the target classes, providing a reliable basis for model training.

# Phase 3: Training & Integration
Models Used:
- Logistic Regression
- KNN
- SVM.

Best Performing Model: 
- Logistic Regression (typically the most stable classifier for this specific cardiovascular dataset).
- Why?:
    - Logistic Regression is the most stable and effective choice for this dataset for three main reasons:
         - Linear Relationships: Your correlation heatmap shows that clinical features (like age and cholesterol) have a direct linear relationship with heart disease risk. Logistic Regression is built specifically to model these linear trends.

        - Clinical Interpretability: In a medical context, we must explain why a prediction was made. Logistic Regression provides clear coefficients, allowing you to show exactly how much each health factor (like age or blood pressure) contributes to the risk score.

        - Computational Efficiency: With 70,000 records, Logistic Regression is significantly faster and more memory-efficient than complex models like SVM or KNN, while still delivering high accuracy.

How to Run
- Set up a virtual environment: python -m venv myenv

- Install requirements: pip install -r requirements.txt

- Execute notebooks in order (Phase 1 -> Phase 2 -> Phase 3).