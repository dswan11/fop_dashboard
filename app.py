import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
data = pd.read_csv('16Jul_Results.csv')

data2 =pd.read_csv('merged_data.csv')


    # Streamlit app
st.title("FOP Analysis Dashboard V2")
st.write("This page displays data from a learnign session.")

# Create three columns for the pie charts
col1, col2, col3 = st.columns(3)

# Ensure the data has the correct format
# Create a radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=data['Score'],
    theta=data['Parameter'],
    fill='toself'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )),
    showlegend=False
)

# Streamlit app
#st.title("Radar Chart Example")
#st.write("This radar chart visualizes the data points from the CSV file.")



#st.plotly_chart(fig)

# Create the first pie chart
fig1 = px.pie(data2, names='speaker', values='wait_time', title='Wait Time')

    # Create the second pie chart
fig2 = px.pie(data2, names='speaker', values='t_duration', title='Speaking duration')



col1.plotly_chart(fig)
col2.plotly_chart(fig1)
col3.plotly_chart(fig2)

# Display the first pie chart
#st.plotly_chart(fig1)

# Display the second pie chart
#st.plotly_chart(fig2)
