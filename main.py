import streamlit as st
import numpy as np
from data.daily import *
from data.weekly import *
from data.monthly import *
from data.annually import *
from data.output import *
from PIL import Image, ImageDraw, ImageFont

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


text1 = "Create Image"
text2 = 'With Python'
img_name = 'Output.png'
background= Image.open('./data/Background.jpg')
color = 'dark_blue'  # grey,light_blue,blue,orange,purple,yellow,green
font = 'Roboto-Bold.ttf'
background = write_image(background, colors[color], text1, text2)
background.save(img_name)

with open("Output.png", "rb") as file:
    btn = st.download_button(
            label="Download Output",
            data=file,
            file_name="Output.png",
            mime="image/png"
          )
