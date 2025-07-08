# 🧠 ML Model Folder Structure (Personal Preference)

This repository contains the structure I personally prefer for organizing Machine Learning projects, with a focus on modularity, reproducibility, and clarity.

---

## 📁 Folder Structure Overview

```bash
.
├── data_analysis/
│   └── eda/
│       ├── basic_data_inspection.py
│       ├── bivariate_analysis.py
│       ├── missing_values_analysis.py
│       ├── multivariate_analysis.py
│       ├── univariate_analysis.py
│       └── EDA.ipynb
├── data_source/
├── pipelines/
├── saved_model/
├── src/
│   ├── data_splitter.py
│   ├── feature_engineering.py
│   ├── handle_missing_values.py
│   ├── ingest_data.py
│   ├── model_building.py
│   ├── model_evaluator.py
│   └── outlier_detection.py
├── steps/
├── tests/
├── README.md
├── run_deployment.py
├── run_pipeline.py
├── sample_predict.py
├── requirements.txt
└── .gitignore
```

---

## 🧪 Folder Descriptions

### `data_analysis/eda/`

Contains all scripts and notebooks for Exploratory Data Analysis (EDA):

- `basic_data_inspection.py` – general structure, types, and overview of the dataset.
- `univariate_analysis.py` – distribution of individual variables.
- `bivariate_analysis.py` – relationship between two variables.
- `multivariate_analysis.py` – interaction among multiple variables.
- `missing_values_analysis.py` – detection and handling of missing data.
- `EDA.ipynb` – interactive EDA in Jupyter Notebook.

### `data_source/`

Placeholder for raw or processed datasets (not committed to version control unless small sample/test sets).

### `pipelines/`

Contains pipeline definitions (e.g., ZenML or any orchestrated ML flow).

### `saved_model/`

Houses serialized/trained models ready for deployment or evaluation.

### `src/`

Holds core logic for the ML workflow:

- `data_splitter.py` – functions for splitting data into train/validation/test sets.
- `feature_engineering.py` – transformation and encoding logic.
- `handle_missing_values.py` – strategies for missing data imputation.
- `ingest_data.py` – data loading and ingestion methods.
- `model_building.py` – model initialization and training logic.
- `model_evaluator.py` – metrics and evaluation routines.
- `outlier_detection.py` – logic for detecting and managing outliers.

### `steps/`

Modular steps for ZenML or other pipeline orchestrations (e.g., loading, training, evaluating, etc).

### `tests/`

Unit tests and integration tests for validating individual components.

---

## 🚀 Main Scripts

- `run_pipeline.py` – Main entry point to execute the full training pipeline.
- `run_deployment.py` – Script to deploy the model or pipeline.
- `sample_predict.py` – Script to test predictions using a sample input.

---

## 📦 Setup Instructions

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ✅ Notes

- This structure supports **clean separation of concerns** across the ML lifecycle.
- Organized to scale from notebooks to production-ready pipelines.
- Follows personal preferences and experience in developing ML solutions.

---

> 🛠️ Feel free to modify this structure based on your specific project needs and toolsets (e.g., ZenML, MLFlow, Airflow, etc.)

---

## 📱 Follow Me

Stay connected and follow me on my social media networks:

- **Website**: [mulan.co.ke](https://mulan.co.ke/)
- **Facebook**: [Mulan Technologies](https://www.facebook.com/mulantech)
- **Twitter**: [@mulantech](https://twitter.com/mulantech)
- **YouTube**: [Mulan Technologies Channel](https://www.youtube.com/channel/UCp0mCqz5l4HsUk3OEwm4S4Q)
- **LinkedIn**: [Anuary Mulombi](https://www.linkedin.com/in/mulombiannuar/)
- **GitHub**: [mulombiannuar](https://github.com/mulombiannuar)
