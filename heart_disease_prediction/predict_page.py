import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data=load_model()
model = data["model"]
columns = data["columns"]
X_train = data["X_train"]
X_test = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]

def show_predict_page():
    st.title("HEART DISEASE PREDICTION")

    st.write("""### health information/data """)
    
 
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.number_input("Chest Pain Type (CP)", min_value=0, max_value=3, value=0)
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=0, max_value=300, value=120)
    chol = st.number_input("Serum Cholesterol (chol)", min_value=0, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [True, False])
    restecg = st.number_input("Resting Electrocardiographic Results (restecg)", min_value=0, max_value=2, value=0)
    thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0, max_value=220, value=150)
    exang = st.selectbox("Exercise Induced Angina (exang)", [True, False])
    oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.number_input("Slope of the Peak Exercise ST Segment (slope)", min_value=0, max_value=2, value=0)
    ca = st.number_input("Number of Major Vessels (ca)", min_value=0, max_value=4, value=0)
    thal = st.selectbox("Thalassemia (thal)", ["Normal", "Fixed Defect", "Reversible Defect"])

    if st.button("Predict"):
        # Process user inputs
        sex_encoded = 1 if sex == "Male" else 0  # Manually encode sex to 1 for Male and 0 for Female
        thal_encoded = 0 if thal == "Normal" else 1 if thal == "Fixed Defect" else 2  # Manually encode thal
        fbs_numeric = 1 if fbs else 0
        exang_numeric = 1 if exang else 0
        
        user_inputs = np.array([
            age, sex_encoded, cp, trestbps, chol, fbs_numeric, restecg, thalach, exang_numeric, oldpeak, slope, ca, thal_encoded
        ]).reshape(1, -1)


    

        try:
            
            prediction = model.predict(user_inputs)
            prediction_label = "Heart Disease" if prediction[0] == 0 else "No Heart Disease"
            st.success(f"The prediction is: {prediction_label}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
