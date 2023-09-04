from financetoolkit import Toolkit
import streamlit as st

companies = Toolkit(['AAPL', 'MSFT'], api_key='e1f7367c932b9ff3949e05adf400970c' , start_date='2017-12-31')

# a Historical example
historical_data = companies.get_historical_data().head()
st.dataframe(historical_data)