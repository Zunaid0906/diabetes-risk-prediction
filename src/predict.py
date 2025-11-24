import joblib
import numpy as np

def load_model():
    model = joblib.load("./models/best_model.pkl")
    scaler = joblib.load("./models/scaler.pkl")
    return model, scaler

def get_user_input():
    print("Enter the following details:")

    pregnancies = float(input("Pregnancies: "))
    glucose = float(input("Glucose: "))
    blood_pressure = float(input("Blood Pressure: "))
    skin_thickness = float(input("Skin Thickness: "))
    insulin = float(input("Insulin: "))
    bmi = float(input("BMI: "))
    dpf = float(input("Diabetes Pedigree Function: "))
    age = float(input("Age: "))

    features = [pregnancies, glucose, blood_pressure,
                skin_thickness, insulin, bmi, dpf, age]

    return np.array(features).reshape(1, -1)

def main():
    model, scaler = load_model()
    user_features = get_user_input()

    # scale the input
    user_features_scaled = scaler.transform(user_features)

    # predict
    prediction = model.predict(user_features_scaled)[0]
    proba = model.predict_proba(user_features_scaled)[0][1]

    if prediction == 1:
        print(f"\n⚠️ HIGH RISK of diabetes (probability: {proba:.2f})")
    else:
        print(f"\n✅ LOW RISK of diabetes (probability: {proba:.2f})")

if __name__ == "__main__":
    main()
