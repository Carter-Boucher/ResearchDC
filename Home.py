import streamlit as st
import pandas as pd
import numpy as np
import snowflake as sf
#from snowflake import snowpark as sp

st.set_page_config(
    # layout="wide",
    initial_sidebar_state="expanded",
    page_title="Home",
    page_icon="📊",
)

st.title('Raw Data Collection Project')
st.write("Carter Boucher")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10)
#displays the raw data
st.subheader('Raw data')
st.write(data)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

#creates a histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#creates a map
st.subheader('Map of all pickups')
st.map(data)

#creates a checkbox
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


#creates a selectbox
#option = st.selectbox(
#    'Which number do you like best?',
#        data[DATE_COLUMN],
#        data[DATE_COLUMN].dt.hour,
#    key='1')
#'You selected: ', option, 'hour', 
#data[DATE_COLUMN].dt.hour[option], 'o\'clock', 
#data[DATE_COLUMN].dt.minute[option], 'minutes', 
#data[DATE_COLUMN].dt.second[option], 'seconds'


# #creates a slider
# st.subheader('Number of pickups by hour')
# #show all data
# st.write(data)
# hour_to_filter = st.slider('hour', 0, 23, 17)
# #show data from hour 0 to hour_to_filter
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.write(hour_to_filter)
# st.write(filtered_data)

#creates a button
if st.button('Say hello'):
    st.write('Why hello there')
# else:
#     st.write('Goodbye')

#when the button is clicked go to page plotting demo
if st.button('Go to page "Plotting Demo"'):
    st.markdown(
        """
        # This is a new page
        """
    )
    st.write

#creates a text input
title = st.text_input('Movie title')
st.write('The current movie title is', title)



filer = st.text_input("hour to filter")
filtered_data = data[data[DATE_COLUMN].dt.hour == filer]
st.write(filtered_data)