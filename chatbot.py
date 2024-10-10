import os
import google.generativeai as genai
import streamlit as st

from dotenv import load_dotenv
from MarketData import fetch_latest_data_to_dataframe

#from MarketData.py a database fetch
df = fetch_latest_data_to_dataframe()

# Set API key for Google Generative AI
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model with generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

#Fine tune prompt from google studio
system_instruction = (
    "Only Filipino food recipe, add price in the recipe. "
)


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=system_instruction
)

# Add the data to conversation by appending to history
history = [
    {
        "role": "model",
        "parts": [
            "This is the current market data from the city of metro manila market you can use this for pricing the recipe:",
            df.to_json(orient='records')
        ]
    }
]

# Streamlit UI setup
st.title("💬 Mealbot")
st.info("👨‍🍳This bot is equipped with the latest market data, ensuring that users have access to up-to-date information on market prices.👨‍🍳")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display the chat history in the Streamlit app
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input for the chatbot
if user_input := st.chat_input("ANONG ULAM GUSTO MO?"):
    # Append user input to the session state messages
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Start a chat session with the Google Generative AI model
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)

    # Extract the model's response and update the session state
    model_response = response.text
    st.session_state["messages"].append({"role": "assistant", "content": model_response})

    # Display the model's response
    st.chat_message("assistant").write(model_response)

    # Update the conversation history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
