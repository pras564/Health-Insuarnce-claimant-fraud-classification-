#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import streamlit as st 
from sklearn.ensemble import RandomForestClassifier 
from pickle import dump 
from pickle import load


# In[5]:


st.title('Model Deployment: Classification')
st.sidebar.header('User Input Parameters')
    





def user_input_features():
    Admission_type = st.sidebar.selectbox("Admission Type",("Elective","Urgent","Emergency","Newborn"))
    if Admission_type=="Elective":
        Admission_type = 0
    elif Admission_type=="Emergency":
        Admission_type = 1
    elif Admission_type=="Newborn":
        Admission_type = 2
    elif Admission_type=="Urgent":
        Admission_type = 3
    elif Admission_type=="Not Available":
        Admission_type = 4 
    Tot_charg = st.sidebar.number_input("Insert Total Charge")
    Days_spend_hsptl = st.sidebar.number_input("Insert Number of Days spent in hospital")
    Surg_Description = st.sidebar.selectbox("Surg_Description",("Medical","s+urgical"))
    if Surg_Description =="Medical":
        Surg_Description = 0
    elif Surg_Description == "surgical":
        Surg_Description = 1
    ccs_procedure_code =st.sidebar.slider("Select a ccs_procedure_code", 1 , 231)
    st.sidebar.text('Selected: {}'.format(ccs_procedure_code))
    Tot_cost =st.sidebar.number_input("Insert Total cost")
    Payment_Typology= st.sidebar.selectbox("Insert Payment Typology",(1,2,3))
    Weight_baby = st.sidebar.number_input("Insert Baby Weight")
    Home_or_self_care = st.sidebar.selectbox("Select",("Cancer Center or Children's Hospital","Expired","Facility w/ Custodial/Supportive Care","Home or Self Care","Home w/ Home Health Services","Hosp Basd Medicare Approved Swing Bed","Hospice - Home","Hospice - Medical Facility","Inpatient Rehabilitation Facility","Left Against Medical Advice","Psychiatric Hospital or Unit of Hosp","Short-term Hospital","Skilled Nursing Home"))
    if Home_or_self_care == "Cancer Center or Children's Hospital":
        Home_or_self_care = 0
    elif Home_or_self_care == "Expired":
        Home_or_self_care = 1
    elif Home_or_self_care == "Facility w/ Custodial/Supportive Care":
        Home_or_self_care = 2 
    elif Home_or_self_care == "Federal Health Care Facility":
        Home_or_self_care = 3
    elif Home_or_self_care == "Home or Self Care":
        Home_or_self_care = 4 
    elif Home_or_self_care == "Home w/ Home Health Services":
        Home_or_self_care = 5 
    elif Home_or_self_care == "Hosp Basd Medicare Approved Swing Bed":
        Home_or_self_care = 6 
    elif Home_or_self_care == "Hospice - Home":
        Home_or_self_care = 7 
    elif Home_or_self_care == "Hospice - Medical Facility":
        Home_or_self_care = 8 
    elif Home_or_self_care == "Inpatient Rehabilitation Facility":
        Home_or_self_care = 9 
    elif Home_or_self_care == "Left Against Medical Advice":
        Home_or_self_care = 10
    elif Home_or_self_care == "Psychiatric Hospital or Unit of Hosp":
        Home_or_self_care = 11
    elif Home_or_self_care == "Short-term Hospital":
        Home_or_self_care = 12 
    elif Home_or_self_care == "Skilled Nursing Home":
        Home_or_self_care = 13
        
    data={'Admission_type': Admission_type, 
          'Tot_charg':Tot_charg, 
          'Days_spend_hsptl':Days_spend_hsptl,
          'Surg_Description':Surg_Description,
          'ccs_procedure_code':ccs_procedure_code,
          'Tot_cost':Tot_cost,
          'Payment_Typology':Payment_Typology,
          'Weight_baby':Weight_baby,
          'Home_or_self_care':Home_or_self_care}
    
    features = pd.DataFrame(data,index=[0])
    return features


# In[35]:


df=user_input_features()
st.subheader('User Input parameters')
st.write(df)


# In[36]:


load_model = load(open('Fraud_Classification.pkl','rb'))
prediction = load_model.predict(df)
prediction_proba = load_model.predict_proba(df)
if st.button("Prediction"):
   st.success('The claminat is Genuine' if prediction_proba[0][1] > 0.5  else 'The claimant is Fraud')



st.subheader('Prediction Probability')
st.write(prediction_proba)


    


# In[ ]:




