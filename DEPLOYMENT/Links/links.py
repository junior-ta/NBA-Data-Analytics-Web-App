import streamlit as st
from st_function import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Links/pic.png'),)

st.header('Junior Tadiffo, BS Computer Science')

st.info('Undergraduate student researcher, Sports Analytics practitioner and IBM Z Student Ambassador')
        #'more info st.page_link("Who_am_I.py", label="here")')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/juniorta/', 'Follow me on LinkedIn', icon_size)
st_button('cup', 'https://www.paypal.me/juniortadiffo', 'Donate', icon_size)
