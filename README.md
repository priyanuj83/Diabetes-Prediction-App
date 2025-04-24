# 🩺 Diabetes Prediction App

🎯 **[Click here to use the live app](https://diabetes-prediction-app-c2jq6gax9fprfqicwnusbj.streamlit.app/)**

This project uses machine learning to predict whether an individual is diabetic or not based on medical diagnostic features. It is built using the Pima Indians Diabetes dataset and deployed as an interactive web app using **Streamlit**.

---

## 📌 Objective

To build a robust and interpretable machine learning model that can assist in the **early prediction of diabetes**, aiding healthcare professionals in screening high-risk patients more effectively.

---

## 📂 Dataset Overview

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes)
- **Samples:** 768
- **Features:** 8 input attributes + 1 target label (`Outcome`)

| Feature                 | Description                                      |
|------------------------|--------------------------------------------------|
| Pregnancies            | Number of times pregnant                         |
| Glucose                | Plasma glucose concentration                     |
| BloodPressure          | Diastolic blood pressure (mm Hg)                 |
| SkinThickness          | Triceps skin fold thickness (mm)                 |
| Insulin                | 2-Hour serum insulin (mu U/ml)                   |
| BMI                    | Body mass index                                  |
| DiabetesPedigreeFunction | Diabetes heredity function                     |
| Age                    | Age in years                                     |
| Outcome                | Target variable (1 = diabetic, 0 = non-diabetic) |

---

## 🔍 Exploratory Data Analysis

- Replaced invalid zero values with median values in columns like `Glucose`, `BloodPressure`, etc.
- Checked for outliers using IQR method and visualized with boxplots.
- Identified class imbalance (35% positive cases).
- Generated correlation heatmap to understand feature relationships.

---

## 📊 Pattern Discovery with Association Rule Mining

Beyond predictive modeling, this project also implements **Frequent Itemset Mining** using the **Apriori algorithm** to uncover interpretable, high-confidence patterns among diabetic patients.

### 🔎 Why Use It?
Association rule mining helps uncover **co-occurring medical characteristics** that may indicate a higher likelihood of diabetes — offering domain experts a transparent view into the data.

### 🧮 Process:

- Selected meaningful medical features: `Glucose`, `BloodPressure`, `BMI`, and `Age`.
- Binned continuous variables into categories (e.g., `"Glucose=High"`, `"BMI=Obese"`).
- Filtered dataset to include only diabetic patients (`Outcome = 1`).
- Used **`mlxtend.apriori`** and **`association_rules`** to mine and analyze rules with:
  - **min_support** = 0.2
  - **min_confidence** = 0.9

### 📌 Example Rule:
> **If:** `BMI = Obese` **AND** `Age = Older`  
> **Then:** `Glucose = High`  
> - **Support:** 0.27  
> - **Confidence:** 0.91  
> - **Lift:** 1.42

This rule suggests that older individuals with high BMI are highly likely to also show elevated glucose levels — a useful insight for preemptive diagnostics.

### 📦 Libraries Used:
- `mlxtend.frequent_patterns`
- `TransactionEncoder`
- `apriori`
- `association_rules`

This module complements the prediction pipeline by offering **interpretable, unsupervised insights** into the diabetic population.

---

## 🧠 Models Applied

| Model                 | Libraries Used       | Tuning Used          |
|----------------------|----------------------|----------------------|
| Logistic Regression  | `scikit-learn`       | GridSearchCV         |
| Decision Tree        | `scikit-learn`       | GridSearchCV         |
| Random Forest        | `scikit-learn`       | ✅ Final Model |

---

## 📊 Model Evaluation

| Metric              | Logistic Regression | Decision Tree | Random Forest |
|---------------------|---------------------|----------------|----------------|
| Precision (Class 1) | 0.56                | 0.52           | **0.61**       |
| Recall (Class 1)    | **0.85**            | **0.85**       | 0.82           |
| F1-score (Class 1)  | 0.68                | 0.65           | **0.70**       |
| Accuracy            | 0.71                | 0.67           | **0.75**       |

**Conclusion:** Random Forest achieved the best balance between accuracy and recall for diabetic cases. It was selected for deployment.

---

## 🚀 Deployment

The final model is deployed as a **Streamlit web app**.

### 🖥️ Run Locally:

```bash
streamlit run app.py
