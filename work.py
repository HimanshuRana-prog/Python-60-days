import streamlit as st
 
# Set the page configuration
st.set_page_config(page_title="Relevance AI Agent Integration", layout="centered")
 
# App title
st.title("Relevance AI Agent for Canvas Analytics")
 
# Description of the app's purpose
st.write("""
    This app integrates a Relevance AI agent for analyzing text data related to student sentiment.
    The agent can provide insights and recommendations based on the text data you input.
""")
 
# Input for text data
st.header("Enter Text Data")
text_input = st.text_area("Input text related to student feedback or queries:")
 
# Displaying the iframe for the Relevance AI agent
st.header("Relevance AI Agent Analysis")
st.write("""
    The embedded AI agent will analyze the provided text and offer insights and recommendations.
""")
 
# Embed the iframe of the Relevance AI agent
st.components.v1.html(
    """
<iframe src="https://app.relevanceai.com/agents/f1db6c/23e7416f60db-47ff-89b9-749b92fc6d71/cf842e79-36b2-4b6d-a146-bcab189fc2e1/share" 
    width="100%" height="500" frameborder="0"></iframe>
    """,
    height=500
)
 
# Provide a space for users to understand the process
st.write("""
    Input the text above, and the AI agent will process the data through the embedded iframe.
    Use the output to understand the sentiments and recommendations for improving student experiences.
""")
 
# End of the app
st.write("Developed by [Your Name] - Powered by Relevance AI and Streamlit")