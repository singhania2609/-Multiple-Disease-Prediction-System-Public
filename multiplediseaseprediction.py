import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
st.title("Multiple Disease Prediction System")
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.subheader('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies (0–17)', min_value=0, max_value=17, value=3, step=1)
        
    with col2:
        Glucose = st.number_input('Glucose Level (0–199 mg/dL)', min_value=0, max_value=199, value=120, step=1)
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure (0–122 mm Hg)', min_value=0, max_value=122, value=69, step=1)
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness (0–99 mm)', min_value=0, max_value=99, value=20, step=1)
    
    with col2:
        Insulin = st.number_input('Insulin Level (0–846 mu U/ml)', min_value=0, max_value=846, value=79, step=1)
    
    with col3:
        BMI = st.number_input('BMI value (0.0–67.1)', min_value=0.0, max_value=67.1, value=32.0, step=0.1, format="%.1f")
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function (0.078–2.42)', min_value=0.078, max_value=2.42, value=0.47, step=0.01, format="%.3f")
    
    with col2:
        Age = st.number_input('Age of the Person (21–81)', min_value=21, max_value=81, value=33, step=1)
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.subheader('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age (29–77)', min_value=29, max_value=77, value=54, step=1)
        
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
        
    with col3:
        cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3], format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure (94–200 mm Hg)', min_value=94, max_value=200, value=131, step=1)
        
    with col2:
        chol = st.number_input('Serum Cholesterol (126–564 mg/dl)', min_value=126, max_value=564, value=246, step=1)
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        
    with col1:
        restecg = st.selectbox('Resting ECG Results', options=[0, 1, 2], format_func=lambda x: ['Normal', 'ST-T Abnormality', 'LV Hypertrophy'][x])
        
    with col2:
        thalach = st.number_input('Max Heart Rate (71–202 bpm)', min_value=71, max_value=202, value=149, step=1)
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        
    with col1:
        oldpeak = st.number_input('ST Depression (0.0–6.2)', min_value=0.0, max_value=6.2, value=1.0, step=0.1, format="%.1f")
        
    with col2:
        slope = st.selectbox('Slope of Peak Exercise ST', options=[0, 1, 2], format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])
        
    with col3:
        ca = st.selectbox('Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3, 4])
        
    with col1:
        thal = st.selectbox('Thalassemia', options=[0, 1, 2, 3], format_func=lambda x: ['Normal', 'Fixed Defect', 'Reversible Defect', 'Other'][x])
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.subheader("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz) (88–260)', min_value=88.0, max_value=260.2, value=154.2, step=0.1, format="%.3f")
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz) (102–592)', min_value=102.0, max_value=592.1, value=197.1, step=0.1, format="%.3f")
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz) (65–239)', min_value=65.0, max_value=239.2, value=116.3, step=0.1, format="%.3f")
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%) (0.001–0.033)', min_value=0.001, max_value=0.034, value=0.006, step=0.001, format="%.6f")
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs) (0.000007–0.00026)', min_value=0.000007, max_value=0.000260, value=0.000044, step=0.000001, format="%.6f")
        
    with col1:
        RAP = st.number_input('MDVP:RAP (0.0007–0.021)', min_value=0.0006, max_value=0.022, value=0.0033, step=0.0001, format="%.6f")
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ (0.0009–0.020)', min_value=0.0009, max_value=0.020, value=0.0034, step=0.0001, format="%.6f")
        
    with col3:
        DDP = st.number_input('Jitter:DDP (0.002–0.064)', min_value=0.002, max_value=0.065, value=0.010, step=0.001, format="%.6f")
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer (0.01–0.12)', min_value=0.009, max_value=0.120, value=0.030, step=0.001, format="%.6f")
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB) (0.09–1.30)', min_value=0.08, max_value=1.31, value=0.28, step=0.01, format="%.3f")
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3 (0.005–0.056)', min_value=0.004, max_value=0.057, value=0.016, step=0.001, format="%.6f")
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5 (0.006–0.079)', min_value=0.005, max_value=0.080, value=0.018, step=0.001, format="%.6f")
        
    with col3:
        APQ = st.number_input('MDVP:APQ (0.007–0.138)', min_value=0.007, max_value=0.138, value=0.024, step=0.001, format="%.6f")
        
    with col4:
        DDA = st.number_input('Shimmer:DDA (0.014–0.169)', min_value=0.013, max_value=0.170, value=0.047, step=0.001, format="%.6f")
        
    with col5:
        NHR = st.number_input('NHR (0.0007–0.315)', min_value=0.0006, max_value=0.315, value=0.025, step=0.001, format="%.6f")
        
    with col1:
        HNR = st.number_input('HNR (8.4–33.0)', min_value=8.4, max_value=33.1, value=21.9, step=0.1, format="%.3f")
        
    with col2:
        RPDE = st.number_input('RPDE (0.26–0.69)', min_value=0.25, max_value=0.69, value=0.50, step=0.01, format="%.6f")
        
    with col3:
        DFA = st.number_input('DFA (0.57–0.83)', min_value=0.57, max_value=0.83, value=0.72, step=0.01, format="%.6f")
        
    with col4:
        spread1 = st.number_input('spread1 (-7.96 to -2.43)', min_value=-7.97, max_value=-2.43, value=-5.68, step=0.01, format="%.6f")
        
    with col5:
        spread2 = st.number_input('spread2 (0.006–0.450)', min_value=0.006, max_value=0.451, value=0.227, step=0.001, format="%.6f")
        
    with col1:
        D2 = st.number_input('D2 (1.42–3.67)', min_value=1.42, max_value=3.68, value=2.38, step=0.01, format="%.6f")
        
    with col2:
        PPE = st.number_input('PPE (0.045–0.527)', min_value=0.044, max_value=0.528, value=0.207, step=0.001, format="%.6f")
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

def set_bg_from_url(url, opacity=1):
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.875)
