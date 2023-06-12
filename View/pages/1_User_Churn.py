import streamlit as st

st.set_page_config(
    page_title="Web Churn Prediction",
    page_icon=":bar_chart:",
    layout="wide"
    )

st.title("Web Churn Prediction")
st.markdown('---')

if 'disable' not in st.session_state:
    st.session_state.disable = False


name_input = st.text_input('Name', key='Name')


col1, col2 = st.columns(2)

with col1:
    
    gender_input = st.selectbox(
        'Gender',
        ['<select>','Female', 'Male'],
        key='gender_input'
    )
    
    senior_citizen_input = st.selectbox(
        'Senior Citizen',
        ['<select>',0,1],
        key='senior_citizen_input'
    )
    
    partner_input = st.selectbox(
        'Partner',
        ['<select>','Yes', 'No'],
        key='partner_input'
    )
    
    dependents_input = st.selectbox(
        'Dependents',
        ['<select>', 'Yes', 'No'],
        key='dependents_input'
    )
    
    phone_service_input = st.selectbox(
        'Phone Service',
        ['<select>', 'Yes', 'No'],
        key='phone_service_input'
    )
    
    multiple_lines_input = st.selectbox(
        'Multiple Lines',
        ['<select>','Yes', 'No', 'No phone service'],
        key='multiple_lines_input'
    )
    
    internet_service_input = st.selectbox(
        'Internet Service',
        ['<select>', 'DSL', 'Fiber optic', 'No'],
        key='internet_service_input'
    )
    
    online_security_input = st.selectbox(
        'Online Security',
        ['<select>', 'Yes', 'No', 'No internet service'],
        key='online_security_input'
    )

with col2:
    online_backup_input = st.selectbox(
        'Online Backup',
        ['<select>', 'Yes', 'No', 'No internet service'],
        key='online_backup_input'
    )
    
    device_protection_input = st.selectbox(
        'Device Protection',
        ['<select>', 'Yes', 'No', 'No internet service'],
        key='device_protection_input'
    )
    
    tect_support_input = st.selectbox(
        'Tech Support',
        ['<select>', 'Yes', 'No','No internet service'],
        key='tect_support_input'
    )
    
    streaming_tv_input = st.selectbox(
        'Streaming TV',
        ['<select>', 'Yes', 'No','No internet service'],
        key='streaming_tv_input'
    )
    
    streaming_movies_input = st.selectbox(
        'Streaming Movies',
        ['<select>', 'Yes', 'No','No internet service'],
        key='streaming_movies_input'
    )
    
    contract_input = st.selectbox(
        'Contract',
        ['<select>', 'Month-to-month', 'One year', 'Two year'],
        key='contract_input'
    )
    
    paperles_billing_input = st.selectbox(
        'Paperless Billing',
        ['<select>', 'Yes', 'No'],
        key='paperles_billing_input'
    )
    
    payment_method_input = st.selectbox(
        'Payment Method',
        ['<select>', 'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
        key='payment_method_input'
    )
    
monthly_charges_input = st.number_input(
    'Monthly Charges',
    min_value=0.0,
    key='monthly_charges'
)

tenure_input = st.number_input(
    'Tenure',
    min_value=0,
    key='tenure'
)

total_charges_input = st.number_input(
    'Total Charges',
    min_value=0.0,
    key='total_charges'
)

# buttond disabled if name_input is empty
if st.session_state['Name'] == '':
    st.session_state.disable = True
for i in st.session_state:
    if i.endswith('_input'):
        if st.session_state[i] == '<select>':
            st.session_state.disable = True
            break
        else:
            st.session_state.disable = False
            continue
if monthly_charges_input == 0.0:
    st.session_state.disable = True
if tenure_input == 0:
    st.session_state.disable = True
if total_charges_input == 0.0:
    st.session_state.disable = True
 
button_predict_save = st.button(
    label="Predict and Save",
    help="Please fill all the fields" if st.session_state.disable == True else "Click to predict",
    type='primary',
    key="predict_save",
    disabled=st.session_state.disable
)

button_predict = st.button(
    label="Predict",
    help="Please fill all the fields" if st.session_state.disable == True else "Click to predict",
    type='primary',
    key="predict",
    disabled=st.session_state.disable
    )

def on_click_reset():
    st.session_state.Name = ''
    for i in st.session_state:
        if i.endswith('_input'):
            st.session_state[i] = '<select>'
    st.session_state.monthly_charges = 0.0
    st.session_state.tenure = 0
    st.session_state.total_charges = 0.0

button_reset = st.button(
    label="Reset",
    help="Click to reset",
    type='secondary',
    on_click=on_click_reset
)

st.markdown('---')