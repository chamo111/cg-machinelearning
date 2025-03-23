import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('Machine Learning App')
st.write('**Developed by Chamodhie Gamage**')

st.info('This app builds a Machine Learning Model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/chamo111/cg-machinelearning/refs/heads/master/Housing.csv')
  df

  st.write('**X**')
  X_raw = df.drop('price',axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.price
  y_raw

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x = 'area', y = 'bedrooms', color = 'price')

##Input Features
#with st.sidebar:
  #st.header('Input Features')
  #island = st.selectbox('Island', ('Biscoe','Dream','Torgersen'))
  #bill_length_mm = st.slider('Bill Langth (mm)',32.1,59.6,43.9) #st.slider(label, min_value=None, max_value=None, step=None,
  #bill_depth_mm = st.slider('Bill Depth (mm)', 13.1,21.5,17.2)
  #flipper_length_mm = st.slider('Flipper Length (mm)', 172.0,231.0,201.0)
  #body_mass_g = st.slider('Body Mass(g)', 2700.0, 6300.0, 4207.0)
  #gender = st.selectbox('Gender',('male', 'female'))

##create a date frame for the input features
  #data = {'island': island,
       #'bill_length_mm': bill_length_mm,
       #'bill_depth_mm': bill_depth_mm,
       #'flipper_length_mm':flipper_length_mm,
       #'body_mass_g':body_mass_g,
       #'sex': gender}
  #input_df = pd.DataFrame(data,index=[0])
  #input_penguins = pd.concat([input_df,X_raw], axis = 0) #combines two dataframes

#with st.expander('Input Features'):
  #st.write('**Input Penguins**')
  #input_penguins
  #st.write('**Combined Penguin Data**')
  #input_df

##Data Preparations
##encode X
#encode = ['island','sex'] #because they are strings
#df_penguins = pd.get_dummies(input_penguins,prefix=encode) #encoded version
#X = df_penguins[1:]

##df_penguins
#input_row = df_penguins[:1]

#encode y
#target_mapper = {'Adelie': 0,
 #               'Chinstrap': 1,
  #              'Gentoo': 2}
#def target_encode(val):
 # return target_mapper[val]

##y = y_raw.apply(target_encode)
##y
##y_raw



#with st.expander('Data Preparation'):  
 # st.write('**Encoded Input Penguins(X)**')
  #input_row
  #st.write('**Encoded y**')
  #y

## model training
### Train the ML model
#clf = RandomForestClassifier()
#clf.fit(X, y) 

### Apply model to make predictions
#prediction = clf.predict(input_row)
#prediction_proba = clf.predict_proba(input_row)

#df_prediction_proba = pd.DataFrame(prediction_proba)
#df_prediction_proba.columns = ['Adelie','Chinstrap','Gentoo']


##Display Predicted species
#st.subheader('Predicted Species')
#st.dataframe(df_prediction_proba,
 #            column_config = {
  #             'Adelie': st.column_config.ProgressColumn(
   #              'Adelie', 
    #             format='%f',
     #            width='medium',
      #           min_value=0,
       #          max_value=1
        #       ),
 #              'Chinstrap': st.column_config.ProgressColumn(
  #               'Chinstrap', 
   #              format='%f',
    #             width='medium',
     #            min_value=0,
      #           max_value=1
       #        ),
#               'Gentoo': st.column_config.ProgressColumn(
 #                'Gentoo', 
  #               format='%f',
   #              width='medium',
    #             min_value=0,
     #            max_value=1
      #         )
       #      }, hide_index=True)
#df_prediction_proba

#penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
#st.success(str(penguins_species[prediction][0]))










