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
