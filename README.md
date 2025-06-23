## Video Link: https://nileuniversity-my.sharepoint.com/:v:/g/personal/f_maged2245_nu_edu_eg/Eb_zd86PYhNLlzNrDJcCh_0BduzPMdU2UUwEH20xhRpiLQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=CtFvKe
# Predicting Hospital Readmission in Diabetic Patients Using Machine Learning

##  Overview

Hospital readmission is a critical and costly issue in healthcare, particularly for chronic conditions like diabetes. This project leverages machine learning to predict 30-day readmission risk using over 100,000 patient records with clinical, demographic, and treatment-related data.

Three classification models—Logistic Regression, Random Forest, and XGBoost—were trained and evaluated. XGBoost emerged as the top-performing model and was deployed using a lightweight Flask API for real-time prediction.

The project demonstrates how data-driven tools can support early intervention and smarter hospital resource management.

---

##  Model Evaluation

The following models were trained and evaluated on the test set. XGBoost delivered the strongest performance across all metrics:

| Model               | Accuracy | Precision | Recall  | F1 Score |
|--------------------|----------|-----------|---------|----------|
| **XGBoost**         | **0.8893** | **0.8553**  | **0.8893** | **0.8427** |
| Random Forest       | 0.8890   | 0.8735    | 0.8890  | 0.8376   |
| Logistic Regression | 0.8885   | 0.8479    | 0.8885  | 0.8398   |

> ⚖ **Recall Score** was prioritized due to the clinical importance of minimizing false negatives.

---

## 🔧 Best Model Configuration (XGBoost)

After hyperparameter tuning, the optimal configuration for XGBoost was:

```python
n_estimators = 100
max_depth = 10
learning_rate = 0.1
```
Key Features
Exploratory Data Analysis (EDA)

Visualizations were used to uncover trends and inform feature selection:

    Fig. 1: Histogram of readmission rate distribution by age

    Fig. 2: Correlation heatmap between features

Models Compared

    Logistic Regression

    Random Forest Classifier

    XGBoost (final selected model)

Handling Class Imbalance

The dataset was heavily skewed toward non-readmitted patients.
To address this, we used SMOTE (Synthetic Minority Oversampling Technique) to generate synthetic samples and reduce bias.
Evaluation Metrics

    Accuracy

    Precision

    Recall

    F1 Score

    Confusion Matrix
    F1 score was the primary metric for evaluating performance due to the imbalanced nature of the dataset.


📁 Repository Structure
| File                          | Description                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| `CBIO313 Final Project.docx`  | The full scientific report                                                              |
| `Project Notebook Final.html` | Complete Jupyter notebook with code, EDA, model training, and output                    |
| `README.md`                   | This file, providing an overview, setup, and documentation                              |
| `app.py`                      | Flask application that serves the XGBoost model via a web interface                     |
| `diabetic_data.csv`           | The original dataset used for training and evaluation                                   |
| `model.pkl`                   | Serialized XGBoost model used in the deployment app                                     |
| `preprocessor.pkl`            | Serialized preprocessing pipeline (e.g., encoders, imputers, scalers)                   |
| `requirements.txt`            | Python package dependencies required to run the final model                             |

Deployment

The final XGBoost model was deployed using a Flask API (app.py). It accepts patient input data and returns a real-time prediction on whether readmission is likely.




This project requires Python 3.8+ and the following packages:
scikit-learn
xgboost
pandas
flask
imbalanced-learn
matplotlib
seaborn
