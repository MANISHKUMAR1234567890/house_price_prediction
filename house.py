import joblib
import streamlit as st
import pandas as pd

model=joblib.load("D:\ML projects\house_price_prediction\house.pkl")

st.title("House Price Predictor ")

def user_report():
    bedrooms=st.selectbox("Enter number of rooms: ",[1,2,3,4,5,6,7,8,9,10])
    bathrooms=st.selectbox("Enter number of bathrooms required: ",[1,2,3,4,5,6,7,8,9,10])
    sqft_living=st.text_input("Enter area of house in square feet")
    floors=st.selectbox("Enter number of floors: ",[1,2,3])
    yr_built=st.text_input("Enter year in which house is build: ")
    yr_renovated=st.text_input("Enter year in which house is renovated: ")


    user_data={
    'bedrooms' : bedrooms,
    'bathrooms': bathrooms,
    'sqft_living': sqft_living,
    'floors': floors,
    'yr_built': yr_built,
    'yr_renovated' : yr_renovated
    }


    data=pd.DataFrame(user_data, index=[0])
    return data

data=user_report()


if st.button("Predict Price"):
    house_price = model.predict(data)
    st.subheader('The estimated price of this house is approximately ₹ {:.2f}.'.format(house_price[0]))








