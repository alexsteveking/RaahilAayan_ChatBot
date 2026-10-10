import streamlit as st
import random
import time

st.title("Raahil Aayan - Simple Chat")

# Streamed response emulator with keyword checks
def response_generator(user_prompt):
    user_prompt_lower = user_prompt.strip().lower()
    
    # Check for specific intents
    if "hello" in user_prompt_lower or "hi" in user_prompt_lower:
        response = "Hello there! It's great to chat with you. How can I help you today?"
    elif "how are you" in user_prompt_lower:
        response = "I'm doing well, thank you for asking! Ready to help you build some cool Streamlit apps."
    elif "what can you do" in user_prompt_lower:
        response = "I can chat with you, stream responses with a typewriter effect, and handle your conversation history using Streamlit session state!"
    else:
        # Fallback to random responses if no keywords match
        response = random.choice(
            [
                "That's interesting! Tell me more.",
                "Hmm, I'm not entirely sure how to respond to that, but I'm listening!",
                "Do you need help with anything specific?",
            ]
        )
        
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
