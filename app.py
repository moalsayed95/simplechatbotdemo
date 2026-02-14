import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Chatbot")

# Initialize chat history and response tracking
if "messages" not in st.session_state:
    st.session_state.messages = []
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("Message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Stream response from API with conversation history via previous_response_id
    stream = client.responses.create(
        model="gpt-5-nano",
        input=prompt,
        instructions="You are a helpful assistant.",
        previous_response_id=st.session_state.previous_response_id,
        stream=True,
    )
    
    # Yield text deltas and capture response ID
    response_id = [None]
    def stream_text():
        for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta
            elif event.type == "response.completed":
                response_id[0] = event.response.id
    
    with st.chat_message("assistant"):
        response = st.write_stream(stream_text())
    
    st.session_state.previous_response_id = response_id[0]
    st.session_state.messages.append({"role": "assistant", "content": response})
