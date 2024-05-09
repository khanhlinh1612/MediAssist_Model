import pickle

rfc_model = pickle.load(open("models/rfc_model.pkl", 'rb'))

def model_predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    prediction = rfc_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    return int(prediction[0])