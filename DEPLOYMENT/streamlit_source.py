#import pandas as pd
#import csv
#import matplotlib.pyplot as plt
#import os
import streamlit as st
#import base64
#import numpy as np
#import seaborn as sns
#import statsmodels.formula.api as smf


#main_page = st.Page("Main_page.py", title="Main Page")
#pg1= st.Page("page_1_prompt.py", title="prompt 1")
#pg2= st.Page("page_2_prompt.py", title="prompt 2")
#pg3= st.Page("page_3_prompt.py", title="prompt 3")
#pg4= st.Page("page_4_prompt.py", title="prompt 4")
#pg5= st.Page("page_5_prompt.py", title="prompt 5")
#pg6= st.Page("page_6_prompt.py", title="prompt 6")
#pg7= st.Page("page_7_prompt.py", title="prompt 7")
#pg8= st.Page("page_8_pythagoreanExpectation.py", title="Pythagorean Expectation")


pages= {
    "Homepage":[st.Page("Main_page.py", title="Main Page")],
    "Me":[st.Page("Who_am_I.py", title="Who am I?"),
          st.Page("Project's_stack.py", title="Project's stack"),
          st.Page("links-master/links.py", title="Info and Contacts")],
    "Data extraction and visualization":[st.Page("page_1_prompt.py", title="prompt 1"),
                                         st.Page("page_2_prompt.py", title="prompt 2"),
                                         st.Page("page_3_prompt.py", title="prompt 3"),
                                         st.Page("page_4_prompt.py", title="prompt 4"),
                                         st.Page("page_5_prompt.py", title="prompt 5"),
                                         st.Page("page_6_prompt.py", title="prompt 6"),
                                         st.Page("page_7_prompt.py", title="prompt 7")],
    "Analytics":[st.Page("page_8_pythagoreanExpectation.py", title="Pythagorean Expectation")]
}



# Set up navigation
pg = st.navigation(pages, position="hidden")

# Run the selected page
pg.run()