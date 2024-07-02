import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('BestRfModel.pkl', 'rb'))
sc = pickle.load(open('scalar.pkl', 'rb'))

st.header('Heart Disease Prediction')
st.write("""
This app predicts whether a person has Heart disease or not based on their medical data.
""")

st.markdown("""
### Instructions
- **Age**: Age in years
- **Gender**: Male or Female
- **Chest Pain Type**: 4 values (0 to 3)
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **Cholesterol**: serum cholesterol in mg/dl
- **Blood Sugar**: fasting blood sugar > 120 mg/dl(0 or 1)
- **ECG**: resting electrocardiographic results (values 0,1,2)
- **Heart rate**: maximum heart rate achieved
- **Exercise induced angina**: 1= Yes, 0=No
- **Oldpeak**: ST depression induced by exercise relative to rest
- **Slope**: the slope of the peak exercise ST segment
- **Colored by fluoroscopy**: number of major vessels (0-3) colored by flourosopy
- **Thalassemia**: 0 = normal; 1 = fixed defect; 2 = reversable defect
""")
st.markdown("""
### Enter Medical Details:""")
# Input fields for user data
age = st.number_input('Age', min_value=25, max_value=120, value=25, step=1)
gender = st.text_input('Gender', placeholder='Male/Female')
cp = st.number_input('Chest Pain Type', min_value=0, max_value=3, value=0, step=1)
trestbps = st.number_input('Blood Pressure', min_value=90, max_value=200, value=90, step=1)
chol = st.number_input('Cholesterol', min_value=120, max_value=564, value=120, step=1)
fbs = st.number_input('Fasting Blood Sugar', min_value=0, max_value=1, value=0, step=1)
restecg = st.number_input('Rest ECG', min_value=0, max_value=3, value=0, step=1)
thalach = st.number_input('Maximum Heart Rate', min_value=70, max_value=202, value=71, step=1)
exang = st.number_input('Exercise induced angina', min_value=0, max_value=1, value=0, step=1)
oldpek = st.number_input('Old Peak', min_value=0.0, max_value=6.2, value=0.0, step=0.1)
slope = st.number_input('Slope', min_value=0, max_value=2, value=0, step=1)
ca = st.number_input('Colored by fluoroscopy', min_value=0, max_value=3, value=0, step=1)
thal = st.number_input('Thalassemia', min_value=0, max_value=2, value=0, step=1)

# Create a numpy array from the input values
if gender in ['Male', 'male', 'MALE']:
    gender = 1
else:
    gender = 0
user_data = np.array([[age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpek, slope, ca, thal]])

btn = st.button('Click Here to Check')
if btn:
    sc_data = sc.transform(user_data)
    pred = model.predict(sc_data)
    if pred == 1:
        st.write('Person is having Heart Disease')
    else:
        st.write('Congratulations! you are a Healthy Person')
