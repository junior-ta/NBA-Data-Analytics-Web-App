import streamlit as st
from deployment.Links import st_function
from PIL import Image

st_function.load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('deployment/Links/pic.png'),)

st.header('Junior Tadiffo, BS Computer Science')

st.info('Undergraduate student researcher, Sports Analytics practitioner and IBM Z Student Ambassador')
        #'more info st.page_link("Who_am_I.py", label="here")')

st.markdown("""
I am just a chill guy who decided to learn a new language, switch from a french highschool to an english one, passed the IB exam and flew to America to chase his dreams

I am what can be described as a tech jack of all trades. I never shied of expressing my creativity through tech.
I ran YouTube channels with video and audio editing, wrote NBA blogs for a French media source when I was 14, and played around with game development using Scratch, Unity, and Blender. My passion for basketball even led me into data analytics long before I studied it formally. 

Now, as a Computer Science major at the University at Buffalo, I continue to grow my skills through classes and clubs like IBM Z, NSBE, and the Data Analytics Club.
""")

icon_size = 20

st_function.st_button('linkedin', 'https://www.linkedin.com/in/juniorta/', '  Connect on LinkedIn', icon_size)
st_function.st_button('github', 'https://github.com/junior-ta', 'GitHub', 20)
st_function.st_button('email', 'juniorta@buffalo.edu', 'Email Me', 20)
st_function.st_button('instagram', 'https://www.instagram.com/tajr.r.r.r/', 'Instagram', 20)
st_function.st_button('cup', 'https://www.paypal.me/juniortadiffo', '  Donate', icon_size)
