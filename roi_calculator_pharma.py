import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.title('Calculate your ROI with the Lamar Advantage:')


# Create columns for layout
slider_col, data_graph_col = st.columns([1.5, 2.5])


with slider_col:
    drug_cost = st.slider ('Rx List Price ($USD)', min_value=0, max_value=2000, value=575)
    avg_rebate = st.slider ('Average Negotiated Rebate (%)', min_value=0, max_value=100, value=75)
    submissions = st.slider('Total PA Submissions per Year', min_value=0, max_value=1000000, value=70000)
    denials = st.slider('Number of Denials or Incomplete Submissions per Year', min_value=10000, max_value=1000000, value=35000)
    platform_fee = st.slider('Lamar Platform Fee (one time)', min_value=0, max_value=200000, value=100000)
    price_per_auth = st.slider('Cost Per Authorization', min_value=0.0, max_value=40.0, value=35.0)
    number_of_years = st.slider('Years', min_value=0, max_value=10, value=5)

def calculate_roi(submissions, denials, platform_fee, price_per_auth, number_of_years, drug_cost, avg_rebate):
    yearly_cmm_costs = []
    yearly_lamar_costs = []
    yearly_revenue_total = []

    for year in range(1, number_of_years + 1):
        revenue_per_year = float((submissions - denials) * drug_cost * avg_rebate/100)*year/10**6
        yearly_cmm_cost = int(submissions*35*year)/10**6
        yearly_lamar_cost = float(((submissions - denials)*price_per_auth*year) + platform_fee)/10**6
        
        yearly_cmm_costs.append(yearly_cmm_cost)
        yearly_lamar_costs.append(yearly_lamar_cost)
        yearly_revenue_total.append(revenue_per_year)
    
    total_savings = yearly_cmm_costs[-1] - yearly_lamar_costs[-1]
    return yearly_revenue_total, yearly_cmm_costs, yearly_lamar_costs, total_savings

yearly_revenue, yearly_cmm_costs, yearly_lamar_costs, total_savings = calculate_roi(submissions, denials, platform_fee, price_per_auth, number_of_years, drug_cost, avg_rebate)

# Display the numbers in a table
percent_savings = int(yearly_lamar_costs[-1]/yearly_cmm_costs[-1]*100)
data = {
    'Metrics': ['Total Revenue', 'Cost with CoverMyMeds', 'Cost with Lamar Health', 'Total Savings', 'Percent Savings'],
    'Amount (in Millions of Dollars)': [yearly_revenue[-1], yearly_cmm_costs[-1], yearly_lamar_costs[-1], total_savings, percent_savings]
}
with data_graph_col:
    st.write("ROI Metrics for Final Year")
    df = pd.DataFrame(data)
    st.table(df.set_index('Metrics'))

    # Display the graph below the table in the same column
    years = list(range(1, number_of_years + 1))
    fig_line, ax_line = plt.subplots(figsize=(8, 6))
    ax_line.plot(years, yearly_revenue, label='Total Revenue', marker='o')
    ax_line.plot(years, yearly_cmm_costs, label='Cost with CoverMyMeds', marker='o')
    ax_line.plot(years, yearly_lamar_costs, label='Cost with Lamar Health', marker='o')
    ax_line.set_xlabel('Year')
    ax_line.set_ylabel('Total Amount (in Millions of Dollars)')
    ax_line.set_title('A compelling ROI for your ePA needs')
    ax_line.legend()
    st.pyplot(fig_line)




