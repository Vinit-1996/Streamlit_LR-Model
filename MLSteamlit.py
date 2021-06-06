from numpy.lib.function_base import append
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
st.set_option('deprecation.showPyplotGlobalUse', False)

data=pd.read_csv("C:/Users/One/Desktop/Python Finance 2/Streamlit/Salary_Data.csv")
x=np.array(data["YearsExperience"]).reshape(-1,1)
lr=LinearRegression()
lr.fit(x,np.array(data["Salary"]))

st.title("Salary Predictor")

nav=st.sidebar.radio('Navigation',["Home","Prediction","Contribute"])

if nav=="Home":
    no=st.text_input("Enter the No of rows")
    val=st.slider("Filter data using Years ",0,20)
    data=data.loc[data["YearsExperience"]>=val]
    if st.checkbox("Show data"):
        st.table(data.head(int(no)))

    if st.button("Graph"):
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Year of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()

if nav=="Prediction":
    st.header("Know your Salary")
    val=st.number_input("Enter yor Exp ",0.00,20.00,step=0.25)
    val=np.array(val).reshape(1,-1)
    pred=lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your Predicted Salary is {round(pred)}")

if nav=="Contribute":
    st.header("Contribute to our dataset ")
    ex=st.number_input("Enter your Experience ",0.0,20.0)
    sal=st.number_input("Enter your salary",0.0,1000000.0, step=1000.0)
    if st.button("Submit"):
        to_add= {"YearsExperience":[ex],"Salary":[sal]}
        to_add=pd.DataFrame(to_add)
        to_add.to_csv("C:/Users/One/Desktop/Python Finance 2/Streamlit/Salary_Data.csv",mode='a',header=False,index=False)
        st.success("Submitted")

