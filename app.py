from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('back_pain_detection_model.pkl')

# Route for home page (optional, with a form)
@app.route('/')
def home():
    return render_template('index.html')  # Create index.html in templates if you want a form

# Route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data from the request
    pelvic_incidence = float(request.form['Pelvic_Incidence'])
    pelvic_tilt = float(request.form['Pelvic_Tilt'])
    lumbar_lordosis_angle = float(request.form['Lumbar_Lordosis_Angle'])
    sacral_slope = float(request.form['Sacral_Slope'])
    pelvic_radius = float(request.form['Pelvic_Radius'])
    spondylolisthesis_degree = float(request.form['Spondylolisthesis_Degree'])
    pelvic_slope = float(request.form['Pelvic_Slope'])
    direct_tilt = float(request.form['Direct_Tilt'])
    thoracic_slope = float(request.form['Thoracic_Slope'])
    cervical_tilt = float(request.form['Cervical_Tilt'])
    sacrum_angle = float(request.form['Sacrum_Angle'])
    scoliosis_slope = float(request.form['Scoliosis_Slope'])

    # Create feature array
    features = np.array([pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle, sacral_slope,
                         pelvic_radius, spondylolisthesis_degree, pelvic_slope, direct_tilt,
                         thoracic_slope, cervical_tilt, sacrum_angle, scoliosis_slope])

    # Reshape data for a single prediction
    features = features.reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Convert prediction to a readable label
    result = "Abnormal" if prediction[0] == 0 else "Normal"

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
