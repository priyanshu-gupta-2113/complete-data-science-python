## Indian Startup funding details analysis
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='startup analysis')
df=pd.read_csv('indian_startup.csv')
 ## Preprocessing: convert date col to date col and create new col which has ruppess in crore instead of dollars

df.rename(columns={'InvestmentAmount_USD':'Amount'},inplace=True)
## in crore rupees
def to_inr(dollar):
    inr= dollar * 96.5
    return inr/10000000

## to return the name of investor
def load_investor_details(investor):
    st.title(investor)
    ## to return the recent 5 investments of the investor
    last5_df=df[df['Investors'].str.contains(investor)].sort_values(by=['Date'],ascending=False).head()[['Date','Startup','City','Amount']]
    st.subheader('Most Recent Investmenets')
    st.dataframe(last5_df)
    col1,col2= st.columns(2)
    with col1:
        ## to return the largest 5 investements
            big_series=df[df['Investors'].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head(5)
            st.subheader('Top 5 Biggest Investements')
            fig,axs=plt.subplots()
            axs.bar(big_series.index,big_series.values)
            st.pyplot(fig)

    with col2:
         st.subheader("Sectors invested in")
         vertical_series=df[df['Investors'].str.contains(investor)].groupby('Industry')['Amount'].sum()
         vertical_series.plot(kind='pie')
         fig,axs=plt.subplots()
         axs.pie(vertical_series,labels=vertical_series.index,autopct='%0.01f%%')
         st.pyplot(fig)

    
    col1,col2= st.columns(2)
    with col1:
         df['Year']=df['Date'].dt.year
         year_series=df[df['Investors'].str.contains(investor)].groupby('Year')['Amount'].sum()
         fig,axs=plt.subplots()
         axs.plot(year_series.index,year_series.values,linestyle='dotted',color='red',linewidth='1')
         st.pyplot(fig)
         
         
    
def load_overall_analysis():
    st.title('Overall Analysis')
    col1,col2,col3,col4=st.columns(4)
    with col1:
             total=round(df['Amount'].sum())
             st.metric('Total',str(total)+' Cr')
    with col2:
          maxi=round(df['Amount'].max())
          st.metric('Maximum amount',str(maxi)+' Cr')
    with col3:
         average=round(df.groupby('Startup')['Amount'].sum().mean(),1)
         st.metric('Average Funding',average)

    with col4:
         total_startups=df['Startup'].nunique()
         st.metric('Funded Startups',total_startups)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    st.header('MOM Graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
         temp_df=df.groupby(['Year','Month'])['Amount'].sum().reset_index().sort_values(['Year','Month'])
         temp_df['x_axis']=temp_df['Year'].astype(str)+'-'+temp_df['Month'].astype(str)
         fig, axs = plt.subplots()
         axs.plot(temp_df['x_axis'],temp_df['Amount'],color='blue')
         st.pyplot(fig)
    elif selected_option=='Count':
        temp_df=df.groupby(['Year','Month'])['Startup'].count().reset_index().sort_values(['Year','Month'])
        temp_df['x_axis']=temp_df['Year'].astype(str)+'-'+temp_df['Month'].astype(str)
        fig, axs = plt.subplots()
        axs.plot(temp_df['x_axis'],temp_df['Startup'],color='blue')
        st.pyplot(fig)


         


    






   

        
    


df['Amount']=df['Amount'].apply(to_inr)

df['Date']=pd.to_datetime(df['Date'],errors='coerce')

## Project making 
st.dataframe(df)

startups=sorted(df['Startup'].unique().tolist())
investors=sorted(set(df['Investors'].str.split(',').sum()))

st.sidebar.title('Startup Funding Analysis:')
option=st.sidebar.selectbox('Select one',['Overall Analysis','Startup','Inverstor'])

if option=='Overall Analysis':
    ## MOM Chart
    btn0=st.sidebar.button('Show overall Analysis')
    load_overall_analysis()


elif option=='Startup':
    st.sidebar.selectbox('Select Startup',startups)
    btn1=st.sidebar.button('Find Startup Details')
    if btn1:
        st.title('Startup Analysis')

    


else:
    selected_investor=st.sidebar.selectbox('Select Startup',investors)
    btn2=st.sidebar.button('Find investor details')
    st.title('Inverstor Analysis')
    if btn2:
        load_investor_details(selected_investor)











