#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib
import numpy as np
import streamlit as st
import pickle
import xgboost
# In[2]:


#load model



# In[3]:

@st.cache()
# prediction function
def churn_prediction(input_data):
    loaded_model = joblib.load('trained_model_rev.sav')
    input_data_as_array = np.array(input_data)
    input_data_reshape = input_data_as_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)

    if (prediction[0] == 0):
        return 'Not Churn'
    else:
        return 'Churn'


# In[4]:


def main():
    #title
    st.title('Bank Churners Prediction Web App')

    #input
    Customer_Age = st.slider("Age", 1, 100,1) #input angka

    Dependent_count = st.number_input('Dependent Count', step=1) #input angka dari 1-5

    Months_on_book = st.number_input('Month On Book', step=1) #input angka

    Total_Relationship_Count = st.number_input('Total Relationship', step=1) #input angka

    Months_Inactive_12_mon = st.slider('Inactive Month',1,12) #input angka 1-12

    Contacts_Count_12_mon = st.number_input('Number of Contracts', step=1) #input angka 1-12

    Credit_Limit = st.number_input('Credit Limit', step=1) #input angka

    Total_Revolving_Bal = st.number_input('Total Revoling Balance', step=1) #input angka

    Avg_Open_To_Buy = st.number_input('Average Open to Buy Credit Line', step=1) #input angka

    Total_Amt_Chng_Q4_Q1 = st.number_input('Change in Transaction Amount',format="%.3f", step=0.0001) #input angka float

    Total_Trans_Amt = st.number_input('Total Transaction Amount', step=1) #input angka

    Total_Trans_Ct = st.number_input('Total Transaction Count', step=1) #input angka

    Total_Ct_Chng_Q4_Q1 = st.number_input('Change in Transaction Count',format="%.3f", step=0.0001) #input angka float

    Avg_Utilization_Ratio = st.number_input('Average Card Utilization Ratio', step=0.0001)  #input angka float

    Gender_Cat = st.selectbox("Sex",options=['Male' , 'Female']) #input categori (boolean)

    Education_Level_cat = st.selectbox("Education Level",options=['Uneducated' , 
                                                                    'High School',
                                                                    'College',
                                                                    'Graduate',
                                                                    'Post-Graduate',
                                                                    'Doctorate']) #input categori

    Marital_Status = st.selectbox("Marital Status",options=['Single' , 
                                                                    'Married',
                                                                    'Divorced']) #input categori

    Income_Category_cat = st.selectbox("Income Category",options=['Less than $40K' , 
                                                                    '$40K - $60K',
                                                                    '$60K - $80K',
                                                                    '$80K - $120K',
                                                                    'More Than $120K']) #input categori

    Card_Category = st.selectbox("Income Category",options=['Blue' , 
                                                            'Silver',
                                                            'Gold',
                                                            'Platinum']) #input categori

    #input encoders
    #Gender
    #Gender_Cat = 0
    if Gender_Cat == 'Female':
        Gender_Cat = 0
    else:
        Gender_Cat = 1 #Male
    #Education Level
    #Education_Level_cat = 0
    if Education_Level_cat == 'College':
        Education_Level_cat = 0
    elif Education_Level_cat == 'Doctorate':
        Education_Level_cat = 1
    elif Education_Level_cat == 'Graduate':
        Education_Level_cat = 2
    elif Education_Level_cat == 'High School':
        Education_Level_cat = 3
    elif Education_Level_cat == 'Post-Graduate':
        Education_Level_cat = 4
    elif Education_Level_cat == 'Uneducated':
        Education_Level_cat = 5
    #Marital Status
    Marital_Status_Divorced,Marital_Status_Married,Marital_Status_Single = 0,0,0
    if Marital_Status == 'Divorced':
        Marital_Status_Divorced = 1
    elif Marital_Status == 'Married':
        Marital_Status_Married = 1
    elif Marital_Status == 'Single' :
        Marital_Status_Single = 1
    # Income Cat
    #Income_Category_cat = 0
    if Income_Category_cat == 'More Than $120K':
        Income_Category_cat = 0
    elif Income_Category_cat == '$40K - $60K':
        Income_Category_cat = 1
    elif Income_Category_cat == '$60K - $80K':
        Income_Category_cat = 2
    elif Income_Category_cat == '$80K - $120K':
        Income_Category_cat = 3
    elif Income_Category_cat == 'Less than $40K':
        Income_Category_cat = 4
    #Card category
    Card_Category_Blue,Card_Category_Gold,Card_Category_Platinum,Card_Category_Silver = 0,0,0,0
    if Card_Category == 'Blue':
        Card_Category_Blue = 1
    elif Card_Category == 'Gold':
        Card_Category_Gold = 1
    elif Card_Category == 'Platinum':
        Card_Category_Platinum = 1
    elif Card_Category == 'Silver':
        Card_Category_Silver = 1

    #define input array
    prediksi= ''
    predictor =[Customer_Age,Dependent_count,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio,Gender_Cat,Education_Level_cat,Marital_Status_Divorced,Marital_Status_Married,Marital_Status_Single,Income_Category_cat,Card_Category_Blue,Card_Category_Gold,Card_Category_Platinum,Card_Category_Silver]
    #creating prediction button
    if st.button('Evaluate Customer'):
        prediksi = churn_prediction(predictor)
    if prediksi == 'Not Churn':
        st.success("Nasabah tidak berpotensi Churn")
    else:
        st.error("Nasabah berpotensi Churn")
    
if __name__ == '__main__':
    main()


# %%

# %%

# %%

# %%

# %%
