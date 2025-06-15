#import pandas as pd
#import csv
#import matplotlib.pyplot as plt
import os
import sys
import streamlit as st
#import base64
#import numpy as np
#import seaborn as sns
#import statsmodels.formula.api as smf
sys.path.append(os.path.join(os.path.dirname(__file__), 'Links'))

pages= {
    "Homepage":[st.Page("deployment/Main_page.py", title="Main Page")],
    "Me":[st.Page("deployment/Who_am_I.py", title="Who am I?"),
          st.Page("deployment/Project's_stack.py", title="Project's stack"),
          st.Page("deployment/Links/links.py", title="Links")],
    "Data extraction and visualization":[st.Page("deployment/page_1_prompt.py", title="top K leaders bar chart"),
                                         st.Page("deployment/page_2_prompt.py", title="stats of the 5 NBA leaders for X category"),
                                         st.Page("deployment/page_3_prompt.py", title="prompt 3"),
                                         st.Page("deployment/page_4_prompt.py", title="prompt 4"),
                                         st.Page("deployment/page_5_prompt.py", title="prompt 5"),
                                         st.Page("deployment/page_6_prompt.py", title="prompt 6"),
                                         st.Page("deployment/page_7_prompt.py", title="prompt 7")],
    "Analytics":[st.Page("deployment/page_8_pythagoreanExpectation.py", title="Pythagorean Expectation"),
                 st.Page("deployment/page_9_pythagoreanPrediction.py", title="Pythagorean Prediction")]
}



# Set up navigation
pg = st.navigation(pages, position="hidden")

# Run the selected page
pg.run()