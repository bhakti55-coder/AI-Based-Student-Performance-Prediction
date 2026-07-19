# AI-Based Student Performance Prediction 🎓🤖

An end-to-end Machine Learning project that predicts a student's final GPA based on their academic habits, attendance, and support systems, complete with an interactive web interface.

## Project Overview
This project focuses on predicting student performance using artificial intelligence and machine learning techniques. 
This project uses Exploratory Data Analysis (EDA) and a highly accurate **Linear Regression model** (95.32% R-squared accuracy) to identify key factors influencing student success. The analysis revealed that **Absences** heavily negatively correlate with GPA, while **Study Time** and **Parental Support** are the strongest positive indicators.
This project leverages Machine Learning to predict student outcomes. After performing Exploratory Data Analysis (EDA) on a dataset of 2,392 records, a Linear Regression model was trained to achieve **95.32% accuracy**. The project includes a live web application built with Flask, allowing users to input student metrics and receive real-time GPA predictions.

## Key Features
* **Predictive Analytics:** Uses a trained model to forecast student performance.
* **Feature Engineering:** Analyzes key drivers like Study Time, Parental Support, and Absences.
* **Interactive Web App:** A clean, user-friendly Flask interface for instant predictions.
* **Serialized Model:** Uses `pickle` for efficient model deployment.

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
* **Language:** Python 3
* **Backend Framework:** Flask
* **Machine Learning:** Scikit-Learn (Linear Regression), Pandas, NumPy
* **Frontend:** HTML/CSS
* **Deployment:** Local Web Server

## Project Structure
* `app.py`: Main Flask application server.
* `templates/`: Contains `index.html` for the user interface.
* `deployment/`: Contains the serialized model (`student_model.pkl`).
* `src/`: Notebooks and scripts used for EDA and model training.
* `data/`: The primary dataset.

## How to Run
1. **Clone the repository:**
   `git clone <your-repo-url>`
2. **Install dependencies:**
   `pip install Flask pandas numpy scikit-learn`
3. **Run the application:**
   `python app.py`
4. **Access the App:**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

