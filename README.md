**🔍 Features Analyzed:**

Age: Age of the patient.
Sex: Gender (0 = Female, 1 = Male).
Chest Pain Type (CP): Types 0-3.
Resting Blood Pressure (trestbps): mmHg.
Serum Cholesterol (chol): mg/dl.
Fasting Blood Sugar (fbs): >120 mg/dl (0 = No, 1 = Yes).
Resting Electrocardiographic Results (restecg): Results 0-2.
Maximum Heart Rate Achieved (thalach): Maximum rate.
Exercise Induced Angina (exang): (0 = No, 1 = Yes).
ST Depression Induced by Exercise (oldpeak): Relative to rest.
Slope of Peak Exercise ST Segment (slope): Slopes 0-2.
Number of Major Vessels (ca): 0-3.
Thalassemia (thal): (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect).
**🔧 Data Preprocessing:**

1️⃣ Handling Missing Values.
2️⃣ Encoding Categorical Variables (Manual & One-Hot Encoding).
3️⃣ Feature Scaling (Normalization & Standardization).

**📊 Dataset Splitting:**

Split into training and testing sets to ensure robust model evaluation
.
**🤖 Model Training:**

Fitting a Logistic Regression model to discover optimal feature weights and minimize log loss.
📈 Model Evaluation:

Using Accuracy, Precision, Recall, and R2-score to gauge performance and predict heart disease effectively.

**🔍 Model Tuning:**

Adjusting hyperparameters and employing regularization techniques to prevent overfitting and enhance generalization.

**💾 Saving the Model:**

Utilizing pickle to save the trained model and preprocessing steps for deployment in a web app.
🌐 Web Application with Streamlit:

Developed an interactive Streamlit web app allowing users to input health parameters and receive heart disease predictions instantly.
