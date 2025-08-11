import streamlit as st
import joblib
import numpy as np
model =joblib.load("empModel.pkl")
st.title("EMPLOYEE MODEL WHETHER THEY WILL LEAVE APP")
st.divider()
st.write(" this app uses machine learning for predicting whether an employee will leave the company or not, you input values then press predict button")
st.divider()
st.write("Bacherlors = 0")
st.write("Masters = 1")
st.write("PHD = 2") 
Education =st.number_input("Educcation level", min_value= 0, value=0)

PaymentTier =st.number_input("the pay scale level", min_value= 0, value=0)
Gender =st.number_input("Gender of employee", min_value= 0, value=0)
EverBenched =st.number_input("1 for Yes, 0 for No", min_value= 0, value=0)
ExperienceInCurrentDomain =st.number_input("Enter of years of experience", min_value= 0, value=0)

st.divider()
X = [[Education,PaymentTier,Gender,EverBenched,ExperienceInCurrentDomain,]]
predictbutton=  st.button("Predict!")
if predictbutton:
    st.balloons()
    X_array= np.array(X)
    prediction=  model.predict(X_array)
    st.write(f"The Employee {prediction}")

else:
    st.write("please use predict button after entering values")
    #'Education', 'JoiningYear','PaymentTier', 'Age','EverBenched', 'ExperienceInCurrentDomain','YearsOfWork'