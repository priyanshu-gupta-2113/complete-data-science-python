import streamlit as st

st.title('campusx')

col1,col2=st.columns(2)

with col1:
    st.image('airplane.webp')

with col2:
    st.header('Campusx is an online platform')



st.header('courses')
st.header('DSMP')
st.header('DAMP')
st.subheader('DEMP')
st.header('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown(""" 
- Home
- About
- Contact
- Career
- Login
""")


option=st.sidebar.selectbox('Select one',['teacher','student'])
btn=st.sidebar.button('Select')

if btn:
    st.title('Hello'+ option)
