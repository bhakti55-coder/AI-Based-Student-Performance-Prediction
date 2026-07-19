from flask import Flask, request, render_template
import pickle
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load the trained AI model from the deployment folder
with open('deployment/student_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Route 1: Load the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: Handle the form submission and predict
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve all the inputs from the HTML form
    features = {
        'Age': float(request.form['Age']),
        'Gender': float(request.form['Gender']),
        'Ethnicity': float(request.form['Ethnicity']),
        'ParentalEducation': float(request.form['ParentalEducation']),
        'StudyTimeWeekly': float(request.form['StudyTimeWeekly']),
        'Absences': float(request.form['Absences']),
        'Tutoring': float(request.form['Tutoring']),
        'ParentalSupport': float(request.form['ParentalSupport']),
        'Extracurricular': float(request.form['Extracurricular']),
        'Sports': float(request.form['Sports']),
        'Music': float(request.form['Music']),
        'Volunteering': float(request.form['Volunteering'])
    }
    
    # Convert the inputs into a format the model understands (DataFrame)
    input_df = pd.DataFrame([features])
    
    # Generate the prediction
    prediction = model.predict(input_df)[0]
    
    # Send the predicted GPA back to the web page
    return render_template('index.html', prediction_text=f'Predicted GPA: {prediction:.2f} / 4.0')

if __name__ == "__main__":
    # Run the server on port 5000
    app.run(debug=True)