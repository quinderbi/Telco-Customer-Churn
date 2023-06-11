import streamlit as st

multipleLines = ['No phone service', 'No', 'Yes']
InternetService = ['DSL', 'Fiber optic', 'No']
OnlineSecurity = ['No', 'Yes', 'No internet service']
OnlineBackup = ['Yes', 'No', 'No internet service']
DeviceProtection = ['No', 'Yes', 'No internet service']


name_input = st.text_input('Name')

col1, col2 = st.columns(2)

with col1:
    
    gender_input = st.selectbox(
        'Gender',
        ['<select>','Female', 'Male']
    )
    
    senior_citizen_input = st.selectbox(
        'Senior Citizen',
        ['<select>',0,1]
    )
    
    partner_input = st.selectbox(
        'Partner',
        ['<select>','Yes', 'No']
    )
    
    dependents_input = st.selectbox(
        'Dependents',
        ['<select>', 'Yes', 'No']
    )
    
    phone_service_input = st.selectbox(
        'Phone Service',
        ['<select>', 'Yes', 'No']
    )
    
    multipleLines_input = st.selectbox(
        'Multiple Lines',
        ['<select>','Yes', 'No', 'No phone service']
    )
    

with col2:
    tect_support_input = st.selectbox(
        'Tech Support',
        ['<select>', 'Yes', 'No','No internet service']
    )
    
    streaming_tv_input = st.selectbox(
        'Streaming TV',
        ['<select>', 'Yes', 'No','No internet service']
    )
    
    streaming_movies_input = st.selectbox(
        'Streaming Movies',
        ['<select>', 'Yes', 'No','No internet service']
    )
    
    contract_input = st.selectbox(
        'Contract',
        ['<select>', 'Month-to-month', 'One year', 'Two year']
    )
    
    paperles_billing_input = st.selectbox(
        'Paperless Billing',
        ['<select>', 'Yes', 'No']
    )
    
    payment_method_input = st.selectbox(
        'Payment Method',
        ['<select>', 'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    )