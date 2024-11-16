import streamlit as st
from datetime import datetime
import time

# Define the file where the chat history will be stored
CHAT_HISTORY_FILE = 'data.txt'

# Function to read chat history (up to 100 most recent messages)
def read_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, 'r', encoding='utf-8') as f:
            chat_history = f.readlines()
        return chat_history[-100:]  # Return only the last 100 messages
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

# Function to save a new message to the chat history file
def save_message(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_message = f"{current_time}: {message}\n"
    
    # Append the new message to the file
    with open(CHAT_HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(new_message)

# Streamlit App Interface
def main():
    # Initialize session state if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state.messages = read_chat_history()

    # Title of the chat application
    st.title("Anonymous Real-Time Chat")

    # Display chat history in a scrollable text area
    chat_placeholder = st.empty()
    chat_history = "\n".join(st.session_state.messages)
    chat_placeholder.text_area("Chat", value=chat_history, height=300, max_chars=None, key="chat_area", disabled=True)

    # Input box for the new message
    new_message = st.text_input("Your message:")

    # Send button
    if st.button("Send"):
        if new_message:
            save_message(new_message)  # Save the new message to the file
            st.session_state.messages = read_chat_history()  # Reload chat history from the file
            st.success("Your message has been sent!")
        else:
            st.warning("Please enter a message before sending.")

    # Simulate real-time update (poll every 1 second)
    time.sleep(1)  # Delay to simulate "real-time" chat updates
    st.rerun()  # Re-run to refresh the chat

if __name__ == "__main__":
    main()
