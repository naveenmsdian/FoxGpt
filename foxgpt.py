import streamlit as st
import google.generativeai as genai

# Set your API key directly in the code
API_KEY = st.secrets["api"]  # Replace this with your actual API key

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
user_input = st.text_area("Your Input:", height=150)

# Button to generate response
if st.button("Generate Response"):
    if user_input:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)
        
        # Properly format response with 8 words per line, new lines after sentences, and breaks between points
        def wrap_text(text, max_words):
            words = text.split()
            lines = []
            current_line = []

            for word in words:
                current_line.append(word)
                if len(current_line) == max_words:
                    lines.append(" ".join(current_line))
                    current_line = []
                
                # Check if the last word is a period, indicating end of a sentence
                if word.endswith('.'):
                    if current_line:  # Add the current line if not empty
                        lines.append(" ".join(current_line))
                        lines.append("")  # Add an empty line for a break
                        current_line = []
            
            # Add any remaining words to the final line
            if current_line:
                lines.append(" ".join(current_line))
                
            return "\n".join(lines)

        formatted_response = wrap_text(response.text, 8)

        st.write("**Response:**")  # Bold heading
        st.code(formatted_response, language='text')
    else:
        st.warning("Please enter a message before generating a response.")
