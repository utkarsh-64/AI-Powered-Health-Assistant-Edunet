import streamlit as st
import google.generativeai as genai

# Ensure set_page_config() is the first Streamlit command
st.set_page_config(page_title="Healthcare Assistant Chatbot", page_icon="⚕️")

# Configure Gemini API Key
genai.configure(api_key="AIzaSyAbDmTxWhdET90ewn2D7FDeE_IJT8I3ek8")

# Load the Gemini model
model = genai.GenerativeModel("gemini-pro")

def healthcare_chatbot(user_input):
    user_input = user_input.lower()  # Normalize input
    
    predefined_responses = {
        "appointment": "Would you like me to help schedule an appointment with a doctor?",
        "medication": "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor.",
        "emergency": "If this is a medical emergency, please contact emergency services immediately.",
    }

    # Check if user input matches a predefined response
    for key in predefined_responses:
        if key in user_input:
            return predefined_responses[key]

    # If no predefined response, use Gemini model
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return "I'm sorry, but I couldn't process your request. Please try again."

def main():
    st.sidebar.title("About the Chatbot")
    st.sidebar.write("This chatbot provides general healthcare guidance. Always consult a doctor for medical advice.")

    st.title("⚕️ Healthcare Assistant Chatbot")

    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input.strip():
            with st.spinner("Processing your query... Please wait..."):
                response = healthcare_chatbot(user_input)
            st.success("**Assistant:** " + response)
        else:
            st.warning("Please enter a valid healthcare-related query.")

if __name__ == "__main__":
    main()
