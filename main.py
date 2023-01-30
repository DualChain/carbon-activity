import streamlit as st
import numpy as np
from data.daily import *
from data.weekly import *
from data.monthly import *
from data.annually import *

st.markdown("## Carbon Activity - A Dualchain Initiative")

select= st.selectbox('',['Daily','Weekly','Monthly','Annually','Summary'])


intro= st.expander("About")
intro.markdown(
    '''
    - Calculate carbon based on your daily, weekly, monthly and annual activity.
    - Fill in the details as per your choice or choose a summarized version!
    - Get our image output based on your carbon activity.
    - Share it with friends and family!
    '''
)