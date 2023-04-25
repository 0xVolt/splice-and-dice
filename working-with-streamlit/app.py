# Import libraries
import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the application.
st.title('Uber pickups in NYC')

# Load sample data.
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 'Magically' activate the cache to prevent loading the data every time the site is refreshed. 
@st.cache_data
def loadData(numberRows):
    data = pd.read_csv(DATA_URL, nrows=numberRows)
    
    lowercase = lambda x: str(x).lower()
    
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    
    return data


# Create a data loading state for better UI.

# Create a text element and let the reader know the data is loading.
dataLoadState = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = loadData(10000)

# Notify the reader that the data was successfully loaded.
dataLoadState.text('Data Loaded! (Using @st.cache_data)')

# Data viz.

# Write the raw data to the application.
st.subheader('Raw data')
st.write(data)