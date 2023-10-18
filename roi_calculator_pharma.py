import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random


# Function to generate sample data
def generate_sample_data(quarters=5):
    data = {
        "Quarters": [],
        "Submissions": [],
        "Approvals": [],
        "Competitor_Approvals": []
    }
    
    for quarter in range(1, quarters+1):
        year = (quarter-1)//4 + 1
        qtr = (quarter-1)%4 + 1
        
        submissions = random.randint(100, 200) * quarter
        approvals = random.randint(50, submissions)
        competitor_approvals = random.randint(25, approvals)
        
        data["Quarters"].append(f"Y{year}Q{qtr}")
        data["Submissions"].append(submissions)
        data["Approvals"].append(approvals)
        data["Competitor_Approvals"].append(competitor_approvals)
    
    return data

# Streamlit interface
st.title('Prior Authorizations over Quarters')

# Button to generate new sample data
if st.button('Generate Sample Data'):
    sample_data = generate_sample_data()

    # Extracting data
    quarters = sample_data["Quarters"]
    submissions = sample_data["Submissions"]
    approvals = sample_data["Approvals"]
    competitor_approvals = sample_data["Competitor_Approvals"]

    # Creating the graph
    fig, ax = plt.subplots()
    ax.plot(quarters, submissions, label='Number of Submissions', marker='o')
    ax.plot(quarters, approvals, label='Number of Approvals', marker='o')
    ax.plot(quarters, competitor_approvals, label='Competitor Approvals', marker='o')

    ax.set_xlabel('Quarters')
    ax.set_ylabel('# of Prior Authorizations')
    ax.set_title('Prior Authorizations over Quarters')
    ax.legend()
    ax.set_xticklabels(quarters, rotation=45)  # Rotate quarter labels for better visibility

    # Displaying the graph in Streamlit
    st.pyplot(fig)


# Hardcoded data for the Provider Analytics table
provider_analytics_data = {
    "Top Submitters": ["Provider A", "Provider B", "Provider C"],
    "Top Denials": ["Provider X", "Provider Y", "Provider Z"],
    "Top Competing Submitters": ["Competitor 1", "Competitor 2", "Competitor 3"]

# Creating a DataFrame from the hardcoded data
df_provider_analytics = pd.DataFrame(provider_analytics_data)

# Streamlit interface for displaying the table
st.title('Provider Analytics')
st.table(df_provider_analytics)
