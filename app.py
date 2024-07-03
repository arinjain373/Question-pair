import streamlit as st
import helper
import pickle
from joblib import dump, load
import zipfile

# Path to the zip file
zip_file_path = 'model.zip'
model_file_name = 'model.pkl'

# Extract the model file from the zip archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(model_file_name)

# Load the extracted model file
with open(model_file_name, 'rb') as file:
    model = pickle.load(file)


st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    print(query.shape)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
