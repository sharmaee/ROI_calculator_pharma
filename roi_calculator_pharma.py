import streamlit as st
import matplotlib.pyplot as plt

st.title('Calculate your ROI:')

# Create columns for layout
graph_col, slider_col = st.columns([2.5, 1.5])

with slider_col:
    submissions = st.slider('Number of Submissions per Year', min_value=0, max_value=1000000, value=700000)
    denials = st.slider('Number of Denials or Incomplete Submissions per Year', min_value=10000, max_value=1000000, value=300000)
    platform_fee = st.slider('Platform Fee (one time)', min_value=0, max_value=200000, value=100000)
    price_per_auth = st.slider('Price Per Authorization', min_value=0.0, max_value=40.0, value=35.0)
    number_of_years = st.slider('Years', min_value=0, max_value=10, value=2)

def calculate_roi(submissions, denials, platform_fee, price_per_auth, number_of_years):
    yearly_cmm_costs = []
    yearly_lamar_costs = []
    for year in range(1, number_of_years + 1):
        yearly_cmm_cost = int(submissions*35*year)/10**6
        yearly_lamar_cost = float(((submissions - denials)*price_per_auth*year + platform_fee))/10**6
        yearly_cmm_costs.append(yearly_cmm_cost)
        yearly_lamar_costs.append(yearly_lamar_cost)
    
    total_savings = yearly_cmm_costs[-1] - yearly_lamar_costs[-1]
    return yearly_cmm_costs, yearly_lamar_costs, total_savings

yearly_cmm_costs, yearly_lamar_costs, total_savings = calculate_roi(submissions, denials, platform_fee, price_per_auth, number_of_years)

with graph_col:
    years = list(range(1, number_of_years + 1))
    fig_line, ax_line = plt.subplots(figsize=(8, 6))
    ax_line.plot(years, yearly_cmm_costs, label='CoverMyMeds Cost', marker='o')
    ax_line.plot(years, yearly_lamar_costs, label='Lamar Health Cost', marker='o')
    ax_line.set_xlabel('Year')
    ax_line.set_ylabel('Total Amount (in Millions of Dollars)')
    ax_line.set_title('Cost Over Time')
    ax_line.legend()
    st.pyplot(fig_line)

    # Plotting the bar graph right under the line graph
    labels = ['CoverMyMeds Cost', 'Lamar Health Cost', 'Total Savings']
    values = [yearly_cmm_costs[-1], yearly_lamar_costs[-1], total_savings]
    
    fig_bar, ax_bar = plt.subplots(figsize=(8, 6))
    ax_bar.bar(labels, values)
    ax_bar.set_ylabel('Total Amount (in Millions of Dollars)')
    ax_bar.set_title('ROI Metrics for Final Year')
    st.pyplot(fig_bar)



