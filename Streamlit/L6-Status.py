import streamlit as st
import time 
st.image('anime.webp')
st.video('Anime edit.mp4')


st.sidebar.title('Sun Jing Woo Power levels:')


col1,col2,col3=st.columns(3)

with col1:
    st.write('Sung Jin woo is the main protagonist of Solo Levelling. He became beast from zero power level to absolute S level tier')

with col2:
    st.write('Sung Jin Woo was E rank hunter, now he is S rank hunter.')

with col3:
    st.image('sung.webp')

## To show user if login failed
st.error('login failed') # Red color


## to print the success message
st.success('login successful') # Green color

## to print the warning
st.info('18+ content') # blue color 


## Progress bar is used to show the progress (50/100% like this)

# you start with zero 
bar=st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

## suppose user is uploading a file then we add this bar progress

