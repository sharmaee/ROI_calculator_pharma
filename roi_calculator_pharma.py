import streamlit as st
import matplotlib.pyplot as plt

st.title('Calculate your ROI:')

# Create columns for layout
graph_col, slider_col = st.columns([2.5, 1.5])

with slider_col:
    submissions = st.slider('Number of Submissions per Year', min_value=0, max_value=20000000, value=700000)
    denials = st.slider('Number of Denials/Incomplete Submissions per Year', min_value=0, max_value=20000000, value=300000)
    platform_fee = st.slider('Platform Fee (one time)', min_value=0, max_value=200000, value=100000)
    price_per_auth = st.slider('Price Per Authorization', min_value=0.0, max_value=40.0, value=35.0)
    number_of_years = st.slider('Years', min_value=0, max_value=10, value=2)

def calculate_roi(submissions, denials, platform_fee, price_per_auth, number_of_years):
    cmm_cost = int(submissions*35*number_of_years)/10**6
    lamar_cost = float(((submissions - denials)*price_per_auth*number_of_years + platform_fee))/10**6
    total_savings = cmm_cost - lamar_cost
    return cmm_cost, lamar_cost, total_savings

cmm_cost, lamar_cost, total_savings = calculate_roi(submissions, denials, platform_fee, price_per_auth, number_of_years)

# Plotting the bar graph
labels = ['CoverMyMeds Cost', 'Lamar Health Cost', 'Total Savings']
values = [cmm_cost, lamar_cost, total_savings]

with graph_col:
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel('Total Amount (in Millions of Dollars)')
    ax.set_title('ROI Metrics')
    st.pyplot(fig)
