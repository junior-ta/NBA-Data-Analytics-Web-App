import streamlit as st
from deployment.Links import st_function
from PIL import Image

st_function.load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('deployment/Links/pic.png'),)

st.header('Junior Tadiffo, BS Computer Science')

st.info('Undergraduate student researcher, Sports Analytics practitioner and IBM Z Student Ambassador')
        #'more info st.page_link("Who_am_I.py", label="here")')

icon_size = 20

st_function.st_button('linkedin', 'https://www.linkedin.com/in/juniorta/', '  Connect on LinkedIn', icon_size)
st_function.st_button('github', 'https://github.com/junior-ta', 'GitHub', 20)
st_function.st_button('email', 'juniorta@buffalo.edu', 'Email Me', 20)
st_function.st_button('instagram', 'https://www.instagram.com/tajr.r.r.r/', 'Instagram', 20)
st_function.st_button('cup', 'https://www.paypal.me/juniortadiffo', '  Donate', icon_size)
