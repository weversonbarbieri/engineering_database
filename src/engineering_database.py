import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
import os import json 
from google.oauth2 import service_account

# firebase_certificate = 'engineering-database-fs1-firebase-adminsdk-38sc1-c22043566d.json'

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('src/engineering-database-fs1-firebase-adminsdk-38sc1-c22043566d.json')
    firebase_admin.initialize_app(cred)



# Initialize Firestore
db = firestore.client()

@st.cache_data
# Function to add text to Firestore
def add_text(issue, information):
    doc_ref = db.collection(make_name).document(subject)
    doc_ref.set(
        {          
            'Issue': issue,
            'Information': information
        }
    )


tab1, tab2 = st.tabs(["Enter Information", "Information Updated"])

# updated_date = st.sidebar.date_input("Enter the data you updated the information")
with tab1:

    make_options = ['All Makes', 'Chevrolet', 'Ford', 'GMC', 'information']
    make_name = st.selectbox('Make', make_options)

    subjects_options = ['Programming Issues', 'DTCs', 'Security System']
    subject = st.selectbox('Enter the Subject', subjects_options)

    issue = st.text_input("Enter the Issue", key='issue_input')

    information = st.text_area('Enter the information')


    if st.button('Save Text'):
        add_text(issue, information)
        st.success(f'Information added successfully!')

with tab2:

    collections = db.collections()
    collection_list = []
    
    for collection in collections:
        collection_list.append(collection.id)
    make_selected = st.selectbox("Make: ", collection_list)

    subjects_ref = db.collection(make_selected)
    subjects = subjects_ref.get()

    subject_list = []
    for sub in subjects:
        subject_list.append(sub.id)

    subject_selected = st.selectbox("Subject: ", subject_list)
    


    information = db.collection(make_selected).document(subject_selected)
    info_ref = information.get()

    info_dict = info_ref.to_dict()
    issue = info_dict.get('Issue', '')
    information_added = info_dict.get('Information', '')

    st.write(f"Issue: {issue}")
    st.write(f"Information: {information_added}")

# #######



    


# python -m streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\engineering_database\engineering_database.py'




