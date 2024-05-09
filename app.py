from flask import Flask, render_template, request, jsonify
from utils import model_predict
import warnings
from flask_cors import CORS
warnings.filterwarnings('ignore')
app = Flask(__name__)
cors = CORS(app)
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    age = request.form.get('age')
    sex = request.form.get('sex')
    thalach = request.form.get('thalach')
    restecg = request.form.get('restecg')
    exang = request.form.get('exang')
    chol = request.form.get('chol')
    cp = request.form.get('cp')
    trestbps = request.form.get('trestbps')
    fbs = request.form.get('fbs')
    oldpeak = request.form.get('oldpeak')
    slope = request.form.get('slope')
    ca = request.form.get('ca')
    thal = request.form.get('thal')
    prediction = model_predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    return render_template("index.html", prediction=prediction, age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol, fbs=fbs, restecg=restecg, thalach=thalach, exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    age = data['age']
    sex = data['sex']
    thalach = data['thalach']
    restecg = data['restecg']
    exang = data['exang']
    chol = data['chol']
    cp = data['cp']
    trestbps = data['trestbps']
    fbs = data['fbs']
    oldpeak = data['oldpeak']
    slope = data['slope']
    ca = data['ca']
    thal = data['thal']
    prediction = model_predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    return jsonify({'prediction': prediction})  # Return prediction
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
