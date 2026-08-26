import streamlit as st
import pandas as pd
email=st.text_input('Enter your email:')
password= st.text_input("Enter your password:")

btn= st.button("Do the Login")

if btn: ## if the button is pressed
    if email=='priyanshu2113@gmail.com' and password=='1234':
        st.success('Login success')

    else:
        st.error('Login Failed')


number=st.number_input('Enter your age:')

if number >=18:
    st.balloons() ## used to show flying ballons when the condition is applied
date=st.date_input("Enter your date of birth")



## Dropdown 
## st.selectbox(label,[list of numbers/text])

gender=st.selectbox('Mention your gender',['Male','Female','Others'])
st.write('Your gender is:',gender)

## File uploader
## st.file_uploader(Label)

file=st.file_uploader('Upload a csv file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())

