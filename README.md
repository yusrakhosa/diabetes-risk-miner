# 🩺 Diabetes Risk Miner: Aspect-Based Health Risk Analysis & Patient Profiling
**DS311 Data Mining · Fall 2026 · Project Proposal**

An end-to-end data mining and machine learning pipeline using the **CDC Diabetes Health Indicators Dataset** (UCI ID: 891). This project identifies key clinical and lifestyle risk factors, uncovers patient comorbidity clusters, and predicts secondary health complications. Results are served through an interactive Streamlit dashboard.


---

## 📌 Project Overview
Early detection of Type 2 diabetes is critical to prevent severe long-term complications, yet healthcare providers face challenges in manually screening large populations or identifying complex multi-factor risk combinations. This project turns structured survey records into actionable insights: discovering which lifestyle indicators drive risk, clustering patient health profiles, and predicting individual complications.

---

## ❓ Research Questions We Answer

| Research Question | Method and Evaluation |
| :--- | :--- |
| **Q1.** Which clinical and lifestyle factors (BMI, high blood pressure, physical activity, age, etc.) are the strongest predictors of diabetes risk? | Logistic Regression, Random Forest, and XGBoost; evaluated via Macro-F1 and ROC-AUC using 5-fold cross-validation. |
| **Q2.** What are the main patient comorbidity and risk profile clusters within the population, and how do they group across demographic lines? | PCA/SVD dimensionality reduction followed by K-Means clustering; evaluated via silhouette score and elbow method. |
| **Q3.** Can we predict whether a patient will experience severe health complications based on baseline diabetes status and lifestyle factors? | Decision Trees, Random Forest, and Gradient Boosting models; evaluated via Macro-F1 and PR-AUC with a strict leakage check. |

---

## 📊 Dataset (CDC Diabetes Health Indicators)
* **Source:** UCI Machine Learning Repository (Dataset ID: 891) fetched via the `ucimlrepo` library.
* **Features (`X`) & Targets (`y`):** Survey responses detailing binary diabetes/prediabetes status alongside demographic, lifestyle, and clinical health indicators.

```python
from ucimlrepo import fetch_ucirepo  
  
# fetch dataset (ID 891: CDC Diabetes Health Indicators)  
cdc_diabetes_health_indicators = fetch_ucirepo(id=891)  
  
# data (as pandas dataframes)  
X = cdc_diabetes_health_indicators.data.features  
y = cdc_diabetes_health_indicators.data.targets
