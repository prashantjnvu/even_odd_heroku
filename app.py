import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Find whether the given number is odd or even.

This app confirm whether the entred number is even or odd
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    ent_number = st.number_input("ent_number",min_value=0,step=1)
    

    data = {'ent_number': ent_number
            }
    #features = pd.DataFrame(data, index=[0])
    return ent_number

user_number = user_input_features()

st.subheader('User Input parameters')
st.write(user_number)

answer = ''
if (user_number %2 ==0):
  answer = 'even'
else:
  answer = 'odd'

put = 'The number ' + str(user_number) + " is " + answer
st.subheader(put)