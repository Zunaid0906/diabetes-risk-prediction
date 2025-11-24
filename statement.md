# 📘 Project Statement  
## Diabetes Risk Prediction using Machine Learning

---

## 🔍 Problem Description  
Diabetes is one of the most common chronic diseases worldwide. Many individuals remain undiagnosed due to lack of early screening.  
Early detection can prevent severe complications such as kidney failure, cardiovascular diseases, and nerve damage.

This project aims to use **machine learning** to classify whether a person is at **high risk** or **low risk** of diabetes based on simple medical parameters.

---

## 🎯 Objective  
- To build a machine learning model using the **Pima Indians Diabetes Dataset**.  
- To preprocess data, handle missing values, and scale features.  
- To train a classification model capable of predicting diabetes risk.  
- To evaluate model performance using accuracy, precision, recall, and confusion matrix.  
- To deploy a **CLI-based prediction system** allowing users to enter values and get predictions.  

---

## 🧠 Scope of the Project  
- Uses real-world medical dataset with 8 key health indicators.  
- Implements Logistic Regression for classification.  
- Includes a fully documented Jupyter Notebook for training and analysis.  
- Saves the trained model (`best_model.pkl`) and scaler (`scaler.pkl`).  
- Provides a user-friendly Python script (`predict.py`) that predicts diabetes risk from live user input.  

This project is suitable for demonstrating:
- Data preprocessing  
- Model training  
- Model deployment  
- End-to-end ML pipeline  

---

## 📂 Dataset Used  
**Pima Indians Diabetes Dataset**  
Source: Kaggle / UCI ML Repository  

Features include:
- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  
- (Target) Outcome → 0 or 1  

---

## 🛑 Limitations  
- Dataset is relatively small (768 samples).  
- Only Logistic Regression is used (no ensemble models in this version).  
- Predictions are not medical diagnosis — for educational use only.  

---

## ✔ Expected Output  
- `best_model.pkl` → Trained logistic regression model  
- `scaler.pkl` → StandardScaler for feature scaling  
- CLI program (`predict.py`) that outputs:  

