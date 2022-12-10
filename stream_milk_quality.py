import pickle
import streamlit as st

# membaca model
milkquality_model =  pickle.load(open('milkquality_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Milk Quality')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    pH = st.text_input('input nilai PH')

with col1 :
    Temprature = st.text_input('input nilai Temprature ')

with col1 :
    Taste = st.text_input('input nilai Taste')

with col2 :
    Odor = st.text_input('input nilai Odor')

with col2 :
    Fat = st.text_input('input nilai Fat')

with col2 :
    Turbidity = st.text_input('input nilai Turbidity')

with col2 :
    Colour = st.text_input('input nilai Colour')

# code untuk kelompok jenis bunga
milkquality_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Milk Quality'):
    milkquality_prediction = milkquality_model.predict([[pH, Temprature, Taste, Odor, Fat, Turbidity, Colour]])
    if(milkquality_prediction[0] == 0):
       milkquality_diagnosis ='low'
    elif(milkquality_prediction[0]==1):
        milkquality_diagnosis ='medium'
    else :
        milkquality_diagnosis ='high'

st.success(milkquality_diagnosis)
