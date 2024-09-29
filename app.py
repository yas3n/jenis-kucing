import streamlit as st
import joblib
import numpy as np

model = joblib.load('cats_model.pkl')

# Judul aplikasi
st.title("kucing Species Classification")

# Input dari pengguna
st.write("fitur kucing: ")

Age = st.slider('Umur: ', 0, 20)
Weight = st.slider('Berat: ', 0, 10)
Color = st.slider('warna: ', 0, 14)
gender = st.slider('sex', 0, 1)

if st.button('Predict'):
    input_data = np.array([[Age, Weight,Color,gender]])
    prediction = model.predict(input_data)
    
    # Map hasil prediksi ke nama spesies
    species = ['Russian Blue','Norwegian Forest','Chartreux','Persian','Ragdoll'
                'Ocicat','Abyssiian','Oriental','Egyptian Mau','American Shorthair'
                'Bengal','Cornish Rex','British Shorthair','Burmese','Singapura'
                'Maine Coon','Turkish Angora','Himalayan','Sphynx','Manx','Siberian'
                'Birman','Balinese','Devon Rex','Exotic Shorthair','Scottish Fold'
                'Savannah','Munchkin','Siamese','Tonkinese']
    st.write(f"Prediksi Species Kucing : {species[prediction[0]]}")