Dataset Preparation & Exploration
Conducted Exploratory Data Analysis (EDA) on the diabetes dataset, assessing feature distributions and class balance.
Identified significant class imbalance, with class 1 (diabetic cases) comprising less than 10% of the dataset.

Model Selection & Performance Evaluation
Logistic Regression: Applied StandardScaler for normalization. Achieved an accuracy of 95.87% but struggled with recall for diabetic cases (61.2%), leading to high false negatives.
Random Forest: Improved recall (69.1%) and F1-score (0.80), demonstrating better handling of class imbalance through tree-based learning.
XGBoost: Further optimized recall (69.7%) and precision (95.2%), achieving the most balanced classification, with macro-averaged F1-score of 0.89.

Challenges Faced & Solutions
Class Imbalance Impact on Recall: Early models struggled with identifying diabetic cases, resulting in low recall. 
Solution: Introduced ensemble methods (Random Forest, XGBoost) and explored data resampling techniques.

StandardScaler Use for Logistic Regression: Scaling improved convergence but didn’t fully resolve recall issues.  
Solution: Shifted toward tree-based models that don’t require feature scaling.
