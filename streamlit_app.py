import streamlit as st
import pandas as pd

st.title('Machine Learning App')
st.write('**Developed by Chamodhie Gamage**')

st.info('This app builds a Machine Learning Model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species',axis=1)
  X

  st.write('**y**')
  y = df.species
  y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x = 'bill_depth_mm', y = 'body_mass_g', color = 'species')

#Data preparations
#"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender',('male', 'female'))
  bill_length_mm = st.slider('Bill Langth (mm)',32.1,59.6,43.9) #st.slider(label, min_value=None, max_value=None, step=None,
  
