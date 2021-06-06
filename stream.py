import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

#st.title("Vinit Mota")
#st.header("Disha Mota")
#st.markdown("""<h1>Mahendra Mota</h1> <br> #Priti Mota """,True)
#st.sidebar.subheader("Input Parameter")

#data=pd.read_csv("C:/Users/One\Desktop/Python Finance 2/Part 1. Python Programming Fundamentals/stocks.csv")
#st.write(data)

data1=pd.DataFrame(np.random.randn(100,3),columns=['a','b','c'])

#st.line_chart(data1)
#st.area_chart(data1)
st.bar_chart(data1)
#plt.scatter(data1['a'],data1['b'])
#st.pyplot()
name=st.text_input("Name")
address=st.text_area("Address")
date=st.date_input("Birth date")
if st.button("Submit"):
    st.write("Name :",name)
    st.write("Address :",address)
    st.write("Address :",date)

col=st.sidebar.selectbox("Select the column ", data1.columns)
plt.plot(data1['a'],data1[col])
st.pyplot()

