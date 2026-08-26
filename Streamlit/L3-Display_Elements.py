import streamlit as st
import pandas as pd

## You can display your dataframe
df= pd.DataFrame({'name':['Priyansh','Yash','Rishabh'],'marks':[50,60,70],'package':[10,40,50]})

st.dataframe(df)


## metrics - You can create small small cards to display your metric
## st.metric(name of metric, value of metric, percentage (+ or -))
st.metric('Revenue','Rs 3 Lakh','3%')

st.metric('product Value','Rs 5 Lakh','-2%')


## JSON

st.json({'name':['Priyansh','Yash','Rishabh'],'marks':[50,60,70],'package':[10,40,50]})