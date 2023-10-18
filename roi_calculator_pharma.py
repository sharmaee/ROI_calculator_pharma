import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random

# Function to generate sample data
def generate_sample_data(years=10):
    data = {
        "Years": list(range(1, years+1)),
        "Submissions": [],
        "Approvals": [],
        "Competitor_Approvals": []
    }
    
    for year in data["Years"]:
        submissions = random.randint(500, 1000) * year
        approvals = random.randint(300, submissions)
        competitor_approvals = random.randint(200, approvals)
        
        data["Submissions"].append(submissions)
        data["Approvals"].append(approvals)
        data["Competitor_Approvals"].append(competitor_approvals)
    
    return data

# Streamlit interface
st.title('Competition Analytics')

# Button to generate new sample data
if st.button('Generate Sample Data'):
    sample_data = generate_sample_data()

    # Extracting data
    years = sample_data["Years"]
    submissions = sample_data["Submissions"]
    approvals = sample_data["Approvals"]
    competitor_approvals = sample_data["Competitor_Approvals"]

    # Creating the graph
    fig, ax = plt.subplots()
    ax.plot(years, submissions, label='Number of Submissions', marker='o')
    ax.plot(years, approvals, label='Number of Approvals', marker='o')
    ax.plot(years, competitor_approvals, label='Competitor Approvals', marker='o')

    ax.set_xlabel('Years')
    ax.set_ylabel('# of Prior Authorizations')
    ax.set_title('Prior Authorizations over Time')
    ax.legend()

    # Displaying the graph in Streamlit
    st.pyplot(fig)





