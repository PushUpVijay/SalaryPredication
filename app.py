import streamlit as st
import pickle 
import numpy as np

model = pickle.load(open('linear_regression_model.pkl', 'rb'))

st.title('Salary Prediction App')
st.write('This app predicts the salary based on the years of experience')

years_experience= st.number_input('Select years of experience', min_value=0.0, max_value=50.0,value=1.0,step=0.5)


if st.button('Predict Salary'):
    experience_input= np.array([[years_experience]])
    predication = model.predict(experience_input)
    #st.write(f"Predicted salary for {years_experience} years of experience: ${salary[0]:,.2f}")
    
    st.success(f"Predicted salary for {years_experience} years of experience: ${predication[0]:,.2f}")