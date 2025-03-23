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
  X_raw = df.drop('species',axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x = 'bill_depth_mm', y = 'body_mass_g', color = 'species')

#Data preparations
#"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscoe','Dream','Torgersen'))
  bill_length_mm = st.slider('Bill Langth (mm)',32.1,59.6,43.9) #st.slider(label, min_value=None, max_value=None, step=None,
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.1,21.5,17.2)
  flipper_length_mm = st.slider('Flipper Length (mm)', 172.0,231.0,201.0)
  body_mass_g = st.slider('Body Mass(g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender',('male', 'female'))

#create a date frame for the input features
  data = {'island': island,
       'bill_length_mm': bill_length_mm,
       'bill_depth_mm': bill_depth_mm,
       'flipper_length_mm':flipper_length_mm,
       'body_mass_g':body_mass_g,
       'sex': gender}
  input_df = pd.DataFrame(data,index=[0])
  input_penguins = pd.concat([input_df,X_raw], axis = 0) #combines two dataframes

#encode X
encode = ['island','sex'] #because they are strings
df_penguins = pd.get_dummies(input_penguins,prefix=encode)
#df_penguins
input_row = df_penguins[:1]

#encode y
target_mapper = {'Adelie': 0,
                'Chinstrap': 1,
                'Gentoo': 2}
def target_encode(val):
  return target_mapper[val]

with st.expander('Input Features'):
  st.write('**Input Penguins**')
  input_penguins
  st.write('**Combined Penguin Data**')
  input_df
  st.write('**Encoded Input Penguins**')
  input_row





