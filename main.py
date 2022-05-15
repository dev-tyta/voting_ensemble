import streamlit as st
import pickle

voting_pickle = open('voting_ensemble.pickle', 'rb')
map_pickle = open('output_result.pickle', 'rb')

voting_clf = pickle.load(voting_pickle)
unique_mapping = pickle.load(map_pickle)

st.title('Loan Availability Prediction')
st.write('Intro...... ')
