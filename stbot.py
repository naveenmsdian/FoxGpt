import streamlit as st
import google.generativeai as genai

# Set your API key directly in the code
API_KEY = "AIzaSyDXP06LzL5GFmr48-yLk1fG6j2rMI78d-s"  # Replace this with your actual API key

# Configure the API key
genai.configure(api_key=API_KEY)

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Streamlit user interface
st.title("FOX GPT")
st.write("Created by Naveen Kumar")

# Text input for user message
user_input = st.text_area("Your Input:")

# Button to generate response
if st.button("Generate Response"):
    if user_input:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)
        st.write("Response:")
        st.text(response.text)
    else:
        st.warning("Please enter a message before generating a response.")
