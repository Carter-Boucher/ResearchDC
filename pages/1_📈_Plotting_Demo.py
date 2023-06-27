import streamlit as st
import pandas as pd
import numpy as np
import snowflake as sf
#from snowflake import snowpark as sp

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="hello",
    page_icon="1",
)

st.title('Hello')