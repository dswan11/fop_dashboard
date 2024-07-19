import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import openai

st.sidebar.title("Upload CSV Files")
uploaded_file1 = st.sidebar.file_uploader("Upload the Learning Environment File", type="csv", key="file1")
uploaded_file2 = st.sidebar.file_uploader("Upload the Timing Data File", type="csv", key="file2")

if uploaded_file1 is not None and uploaded_file2 is not None:

    # Load data
    data = pd.read_csv(uploaded_file1)

    data2 = pd.read_csv(uploaded_file2)


    # Streamlit app
    st.title("FOP Analysis Dashboard V2")
    st.write("This page displays data from a learning session.")

    # Create three columns for the pie charts
    col1, col2, col3 = st.columns(3)

    # Ensure the data has the correct format
    # Create a radar chart
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=data['Score'],
        theta=data['Parameter'],
        fill='toself',
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False,
        title="Learning Environment Analysis"
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



    display_data = ["Parameter", "Score", "Explanation"]
    data_to_display = data[display_data]
    final_data = data_to_display.reset_index(drop=True)
    st.write("Explanation from ChatGPT:")
    #st.dataframe(final_data)

    st.table(final_data)

else:
    # Show an empty screen with a message if files are not uploaded
    st.title("Please upload two CSV files from the sidebar to display the charts.")