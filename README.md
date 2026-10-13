# 🩺 Diabetes Risk Miner: Discovering Diabetes Risk Factors and Patient Profiles

**DS311 Data Mining · Fall 2026 · Project P05**

An end-to-end diabetes risk-mining pipeline using the **CDC Diabetes Health Indicators Dataset (UCI ID: 891)**. It identifies important lifestyle and clinical risk factors, discovers patient health-profile clusters, and predicts diabetes-related health risks. Results will be presented through an interactive Streamlit dashboard.

🔗 **GitHub repository:** [Diabetes Risk Miner](https://github.com/yusrakhosa/diabetes-risk-miner) · 📓 **Main notebook:** `notebooks/A1_load_and_overview.ipynb` · 🚀 **Live app:** [Add Streamlit link]

---

## 📌 Project overview

Type 2 diabetes is a major public health concern, and early identification of people at risk can help support preventative healthcare. However, manually screening large populations and identifying combinations of lifestyle and clinical risk factors can be challenging.

This project uses data mining and machine learning to analyze health indicators, identify important diabetes risk factors, discover patient groups with similar health profiles, and predict individual health risks. The results will be presented in an interactive dashboard for exploring population-level trends and patient risk profiles.

**Why the CDC Diabetes Health Indicators Dataset?**

The dataset contains structured health survey records with indicators such as Body Mass Index (BMI), high blood pressure, high cholesterol, physical activity, age, and general health status. These features make it suitable for classification, clustering, and risk-factor analysis. The project also has practical value as an exploratory decision-support tool for public health researchers and healthcare professionals.

## ❓ Questions we answer

| # | Research question | Technique |
|---|---|---|
| Q1 | Which clinical and lifestyle factors are the strongest predictors of diabetes risk, and how accurately can we classify high-risk individuals? | Logistic Regression, Random Forest, XGBoost, and feature importance analysis |
| Q2 | What are the main patient health-profile and comorbidity clusters, and how do they differ across demographic groups? | PCA/SVD dimensionality reduction followed by K-Means clustering |
| Q3 | Can we predict secondary health complications, such as cardiovascular issues or poor general health, from baseline health indicators and lifestyle factors? | Decision Tree, Random Forest, and Gradient Boosting classification |

## 📊 Dataset

| | Details |
|---|---|
| **Source** | [CDC Diabetes Health Indicators Dataset — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators) |
| **UCI Dataset ID** | 891 |
| **Category** | Health indicators, diabetes status, lifestyle, and demographics |
| **Format** | Structured survey data loaded into pandas DataFrames |
| **Features** | BMI, high blood pressure, high cholesterol, physical activity, age, general health, and other health indicators |
| **Target** | Diabetes/prediabetes status, with the exact target encoding verified during data inspection |
| **Access method** | Python `ucimlrepo` library |
| **Data processing** | Data-quality checks, feature preparation, class-imbalance handling, and exploratory data analysis |

The dataset is loaded programmatically in Google Colab using the UCI repository API:

```python
from ucimlrepo import fetch_ucirepo

# Fetch the CDC Diabetes Health Indicators dataset
cdc_diabetes_health_indicators = fetch_ucirepo(id=891)

# Load features and target
X = cdc_diabetes_health_indicators.data.features
y = cdc_diabetes_health_indicators.data.targets

# Inspect dataset metadata and variables
print(cdc_diabetes_health_indicators.metadata)
print(cdc_diabetes_health_indicators.variables)
```

The raw dataset is retrieved from the UCI repository rather than manually stored in the project repository. Dataset dimensions, target distribution, missing values, and variable definitions will be verified during data inspection.

## 🔄 Pipeline

```text
Acquire data from UCI
        ↓
Data quality checks and cleaning
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature preparation and imbalance handling
        ↓
Risk classification · Patient clustering · Complication prediction
        ↓
Model evaluation and leakage checks
        ↓
Interpret results and identify risk patterns
        ↓
Interactive Streamlit dashboard
```

The project will use reproducible preprocessing and modeling workflows, fixed random seeds where applicable, comparison against appropriate baseline models, and validation procedures designed to reduce data leakage.

### Evaluation strategy

- **Q1 — Diabetes risk classification:** Macro-F1 and ROC-AUC, compared against a majority-class baseline using five-fold cross-validation.
- **Q2 — Patient clustering:** Silhouette score and the elbow method to select a suitable number of clusters, with comparison against clustering without dimensionality reduction.
- **Q3 — Complication prediction:** Macro-F1 and PR-AUC using a stratified train-test split and a strict data-leakage check.

The final evaluation will report actual measured results once the models have been trained and tested.

## 📁 Repository structure

```text
diabetes-risk-miner/
├── notebooks/
│   ├── A1_load_and_overview.ipynb
│   └── # Additional modeling notebooks
├── src/                  # Shared data and modeling utilities
├── app/                  # Streamlit dashboard
├── outputs/              # Saved models and result files
├── figures/              # EDA charts and evaluation plots
├── reports/              # Proposal and final report
├── requirements.txt
└── README.md
```

*Note: This is the intended repository structure. Update it to match the actual files and folders in the GitHub repository.*

## ▶️ How to run

**Option 1: Google Colab (recommended)**

1. Open the [GitHub repository](https://github.com/yusrakhosa/diabetes-risk-miner).
2. Open a notebook from the `notebooks/` directory in Google Colab.
3. Install the required libraries if they are not already available.
4. Run the notebook cells to fetch the dataset, inspect the data, and execute the implemented analysis.

Install the dataset library if required:

```python
!pip install ucimlrepo
```

**Option 2: Run locally**

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yusrakhosa/diabetes-risk-miner.git
cd diabetes-risk-miner
pip install -r requirements.txt
```

**Run the dashboard**

Once the Streamlit application and its required files are available, run:

```bash
streamlit run app/streamlit_app.py
```

Ensure that the dashboard script, saved models, and dependencies match the actual repository structure before running the command.

## 👥 Team

| Member | Lead role | Responsibilities |
|---|---|---|
| Yusra Khosa | Data Loading Lead | Dataset extraction through the UCI API, initial data inspection, missing-value checks, and sanity checks |
| Zafeer Rajput | Modeling Lead | Diabetes risk classification, model comparison, hyperparameter tuning, and feature importance analysis for Q1 and Q3 |
| Faizan Bukhari | Product & Deployment Lead | Patient health-profile clustering for Q2, Streamlit dashboard development, and final report compilation |

## 🗓️ Milestones

| Milestone | Focus | Status |
|---|---|---|
| 1 | Data loading, quality checks, and initial EDA | Planned / update progress |
| 2 | Data preparation and baseline models | Planned |
| 3 | Core modeling for Q1, Q2, and Q3 | Planned |
| 4 | Model evaluation, leakage checks, and dashboard integration | Planned |
| 5 | Final report, presentation, and project demonstration | Planned |

Update each status as the corresponding work is completed.

## 📝 Contribution log

| Date | Member | What was done |
|---|---|---|
| 2026-10-13 | Yusra Khosa | Project proposal and dataset-loading plan using the UCI repository API |
| To be updated | Zafeer Rajput | Record modeling implementation and evaluation work |
| To be updated | Faizan Bukhari | Record clustering, dashboard, and report progress |

Replace these entries with the actual work completed by each team member.

## 📈 Expected outputs

- A reproducible Google Colab notebook for dataset loading, cleaning, and EDA.
- Comparative diabetes risk classification models with feature importance analysis.
- Patient health-profile clusters identified using dimensionality reduction and K-Means.
- Complication prediction models evaluated using appropriate classification metrics.
- An interactive Streamlit dashboard for population-level exploration and individual risk estimation.
- A final report and presentation describing methodology, findings, limitations, and public health implications.

## ⚖️ Ethics and AI-use disclosure

This project uses the CDC Diabetes Health Indicators Dataset obtained through the UCI Machine Learning Repository. The original dataset source will be cited in the report and repository documentation.

Health-related predictions can be affected by data quality, class imbalance, survey limitations, and model bias. Dashboard outputs are intended for educational, exploratory, and preventative decision-support purposes only. They must not be treated as definitive medical diagnoses or substitutes for professional medical advice.

Data-processing choices, sampling strategies, imbalance-handling methods, assumptions, and model limitations will be documented. External reference material and generative AI assistance will be disclosed according to course requirements.

## 📚 Citation

**Dataset source**

CDC Diabetes Health Indicators. UCI Machine Learning Repository.  
https
