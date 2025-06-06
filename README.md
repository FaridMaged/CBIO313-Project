---

## Model Evaluation

The following models were trained and evaluated on the test set. XGBoost delivered the strongest performance across all metrics:

| Model               | Accuracy | Precision | Recall  | F1 Score |
|--------------------|----------|-----------|---------|----------|
| **XGBoost**         | **0.8893** | **0.8553**  | **0.8893** | **0.8427** |
| Random Forest       | 0.8890   | 0.8735    | 0.8890  | 0.8376   |
| Logistic Regression | 0.8885   | 0.8479    | 0.8885  | 0.8398   |

> ⚖*Recall Score* was prioritized due to the clinical impact of false negatives in medical predictions.

---

## Best Model Configuration (XGBoost)

After hyperparameter tuning, the optimal parameters for the XGBoost classifier were:

```python
n_estimators = 100
max_depth = 10
learning_rate = 0.1


Key Features

    Exploratory Data Analysis (EDA)
    Visualizations such as histograms and correlation heatmaps were used to uncover patterns and guide feature selection.

        Fig. 1: Histogram of readmission rate distribution by age

        Fig. 2: Correlation matrix for key features

    Models Compared

        Logistic Regression

        Random Forest Classifier

        XGBoost (Final chosen model)

    Handling Class Imbalance
    Used SMOTE (Synthetic Minority Over-sampling Technique) to rebalance training data and mitigate bias toward the majority class.

    Evaluation Metrics
    Accuracy, Precision, Recall, F1 Score, and Confusion Matrices. F1 score was prioritized due to the clinical importance of minimizing false negatives.

    Deployment
    Final model deployed using a simple Flask API (app.py) accepting patient inputs and returning predictions in real-time.

Getting Started

    Note: This repo is for demonstration and academic purposes. It does not include sensitive patient data or any live API functionality.

Requirements

    Python 3.8+

    scikit-learn

    xgboost

    pandas

    flask

    imbalanced-learn

    matplotlib / seaborn (for EDA)


