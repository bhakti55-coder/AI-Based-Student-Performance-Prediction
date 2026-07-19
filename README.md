# AI-Based Student Performance Prediction 🎓🤖

An end-to-end Machine Learning project that predicts a student's final GPA based on their academic habits, attendance, and support systems. 

## Project Overview
This project focuses on predicting student performance using artificial intelligence and machine learning techniques. 
This project uses Exploratory Data Analysis (EDA) and a highly accurate **Linear Regression model** (95.32% R-squared accuracy) to identify key factors influencing student success. The analysis revealed that **Absences** heavily negatively correlate with GPA, while **Study Time** and **Parental Support** are the strongest positive indicators.


## Repository Structure
* **data/**: Contains datasets (CSV, JSON, raw data).
* **src/**: Contains Python code and ML models.
* **reports/**: Contains weekly reports and the final report.
* **deployment/**: Contains Docker, API, and hosting configurations.
 
## Folder Structure
* `data/`: Contains the raw and cleaned datasets (`.csv`).
* `src/`: Jupyter Notebooks containing the EDA, data visualizations, and model training code.
* `reports/`: Generated graphs, correlation heatmap and metric summaries.
* `deployment/`: Contains the serialized Machine Learning model (`.pkl`) and backend code for web application integration.

## Tech Stack
* **Language:** Python 3
* **Data Analysis & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Model Serialization:** Pickle

## How to Run (Local Development)
1. Clone this repository.
2. Ensure you have the required libraries installed (`pip install pandas numpy matplotlib seaborn scikit-learn`).
3. Navigate to the `src/` folder and open `01_Data_Exploration.ipynb` in Jupyter Notebook.
4. Run the cells sequentially to view the data pipeline, train the model, and generate the `student_model.pkl` file.

