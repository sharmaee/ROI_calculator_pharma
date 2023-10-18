import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random

# Hardcoded sample data
sample_data = {
    "Quarters": ["Y1Q1", "Y1Q2", "Y1Q3", "Y1Q4", "Y2Q1"],
    "Submissions": [100, 200, 300, 400, 500],
    "Approvals": [50, 100, 150, 200, 250],
    "Competitor_Approvals": [100, 95, 90, 85, 80]
}

# Streamlit interface
st.title('Prior Authorizations Analytics')

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
