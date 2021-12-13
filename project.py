import numpy as np
import pickle
import pandas as pd
from sklearn import datasets
import streamlit as st 
from sklearn.preprocessing import StandardScaler

from PIL import Image



pickle_in = open("ranfor_banking_churn.pkl","rb")
model = pickle.load(pickle_in)
df = pd.read_csv('Dataset_9_-_Banking.csv')
sc = StandardScaler()
def welcome():
    return "Welcome All"


def predict_note_authentication(Credit_Score,Age,Tenure,Balance,Num_Product,HasCrCard,ActiveMember,Estimated_Salary,Geo_France,Geo_Germany,Geo_Spain,Gender_Female,Gender_Male):
  test =  sc.fit_transform([[Credit_Score,Age,Tenure,Balance,Num_Product,HasCrCard,ActiveMember,Estimated_Salary,Geo_France,Geo_Germany,Geo_Spain,Gender_Female,Gender_Male]])
  pred_std = ([[Credit_Score,Age,Tenure,Balance,Num_Product,HasCrCard,ActiveMember,Estimated_Salary,Geo_France,Geo_Germany,Geo_Spain,Gender_Female,Gender_Male]])
  pred= model.predict(pred_std)
  #pred=int(model.predict([[Credit_Score,Age,Tenure,Balance,Num_Product,HasCrCard,ActiveMember,Estimated_Salary,Geo_France,Geo_Germany,Geo_Spain,Gender_Female,Gender_Male]]))
  if pred == 1:
    pred = 'Keluar'
  else :
    pred = 'Bertahan'
  print(pred)
  return pred



def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Churn Detection </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Geo = st.radio("Pilih Geo",('France','Spain','Germany'))
    if Geo == "France":
      Geo_France = 1
      Geo_Germany = 0
      Geo_Spain = 0
    elif Geo == "Spain":
      Geo_France = 0
      Geo_Germany = 0
      Geo_Spain = 1
    else:
      Geo_France = 0
      Geo_Germany = 1
      Geo_Spain = 0
    Gender = st.radio("Pilih Gender",('Laki-Laki','Perempuan'))
    if Gender == "Laki-Laki":
      Gender_Male = 1
      Gender_Female = 0
    
    else:
      Gender_Male = 0
      Gender_Female = 1
    HasCrCard = st.radio("Have Credit Card",("Yes","No"))
    if HasCrCard == "Yes":
      HasCrCard = 1
    else:
      HasCrCard= 0
    ActiveMember = st.radio("Active Member",("Yes","No"))
    if ActiveMember == "Yes":
      ActiveMember = 1
    else : 
      ActiveMember= 0
    Credit_Score = st.text_input("Credit Score")
    Age = st.text_input("Age")
    Tenure = st.text_input("Tenure")
    Balance = st.text_input("Balance")
    Num_Product = st.text_input("Num Of Product")
    Estimated_Salary = st.text_input("Estimated Salary")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Credit_Score,Age,Tenure,Balance,Num_Product,HasCrCard,ActiveMember,Estimated_Salary,Geo_France,Geo_Germany,Geo_Spain,Gender_Female,Gender_Male)
    st.success('The output is {}'.format(result))
if __name__=='__main__':
    main()
