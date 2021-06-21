# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:02:41 2021

@author: chags
"""

import pandas as pd
import streamlit as st
import sklearn
from sklearn import metrics
import os
import altair as alt
import numpy as np

from urllib.error import URLError
import matplotlib.pyplot as plt

import base64




st.title("Kappa Stat Calculator")
st.text("Measuring interrater reliability")
st.sidebar.header("About")
st.sidebar.text("""The kappa stat calculator uses the
power of scikit-learn to quickly
calculate cohen's kappa statistic
between two raters.

Upload a csv file with columns
specifying your raters names or ids.
""")


df = st.file_uploader("Choose a file")
if df:
    df = pd.read_csv(df)

    col1, col2 = st.beta_columns(2)
   
    with col1:
        st.dataframe(df.style.highlight_max(axis=0))  # Same as st.write(df)
   

    with col2:
        st.line_chart(df)
        person1 = st.sidebar.text_input("Enter column name for person 1")
        person2 = st.sidebar.text_input("Enter column name for person 2")
       
   
        if st.sidebar.button("Calculate Kappa Statistic"):
                y1 = df[person1]
                y2 = df[person2]
                kap = sklearn.metrics.cohen_kappa_score(y1, y2,labels=None, weights=None, sample_weight=None)
                st.sidebar.write('Result: %s' % kap)
                st.balloons()

