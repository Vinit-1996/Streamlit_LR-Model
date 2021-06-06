import streamlit as st

st.title("Registration Form")

first,last=st.beta_columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email,mob=st.beta_columns([3,1])
email.text_input("Email")
mob.text_input("Mobile No")

user,pw,pw2=st.beta_columns(3)
user.text_input("Username")
pw.text_input("Password",type="password")
pw2.text_input("Retype Your Password", type="password")

ch,bl,sub=st.beta_columns(3)
ch.checkbox("I Agree")
sub.button("Submit")