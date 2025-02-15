import streamlit as st
import requests
import json

# Function to interact with Gemini Pro API for summarization
def summarize_text(text, api_key):
    url = "https://api.generativeai.google.com/v1alpha/gemini:text:summarize"  # Hypothetical URL for Gemini Pro summarization API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Create the payload (adjust as per API documentation for Gemini Pro)
    payload = {
        "input_text": text,  # Text to be summarized
        "summary_length": "short"  # Options might include "short", "medium", or "long"
    }

    # Sending POST request to Gemini Pro API
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Parsing and extracting the summary from the response
        summary = response.json().get('summary', 'No summary found')
        return summary
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit user interface
st.title("Text Summarization with Gemini Pro API")
st.markdown("Enter the text you want to summarize, and click the button below.")

# Text input for the user to provide the content for summarization
input_text = st.text_area("Enter your text here:")

# Input for Gemini API Key (stored securely in practice, here for simplicity)
api_key = "AIzaSyDm3R3APkK5dqgnSqPYh_m3jHJC2OQKJKU"

# When the user clicks the "Summarize" button
if st.button("Summarize"):
    if input_text and api_key:
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text, api_key)
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.error("Please provide both the text and a Gemini API Key.")
