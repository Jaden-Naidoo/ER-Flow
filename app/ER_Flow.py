from helpers import *
from simulation_page import *
import streamlit as st
import numpy as np
st.set_page_config(page_title='ER Flow', page_icon=':material/emergency:', layout ='wide')

st.sidebar.title(':primary[:material/navigation:] Navigate To')
selected_page = st.sidebar.selectbox(
    '',
    ['Home','Triage Level Prediction','Patient Simulation']
)

if selected_page == 'Home':
    theme_main_page()
    st.title(':material/local_hospital: :primary[ER] Flow')
    st.subheader('AI-powered triage insights for emergency patient flow.')
    feat_cards()

if selected_page == 'Triage Level Prediction':
    predict_page()

if selected_page == 'Patient Simulation':
    sim_page()



