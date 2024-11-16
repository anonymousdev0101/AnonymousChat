import streamlit as st
from datetime import datetime

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
def save_message(username, message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_message = f"{current_time} - {username}: {message}\n"
    
    # Append the new message to the file
    with open(CHAT_HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(new_message)

# Streamlit App Interface
def main():
    # Check if username is stored in session state
    if 'username' not in st.session_state:
        # Ask the user to enter their username
        st.session_state.username = st.text_input("Enter your username:")

    # If username is entered, hide the username input and show chat interface
    if st.session_state.username:
        st.title(f"Welcome, {st.session_state.username}!")
        
        # Display previous chat history (last 100 messages)
        st.subheader("Chat History")
        chat_history = read_chat_history()
        for message in chat_history:
            st.write(message.strip())  # Remove newline character at the end of each message

        # Input box for the new message
        new_message = st.text_input(f"Your message, {st.session_state.username}:")

        # Send button
        if st.button("Send"):
            if new_message:
                save_message(st.session_state.username, new_message)  # Save the new message to the file
                st.success("Your message has been sent!")
                st.experimental_rerun()  # Refresh the app to display the new message in the chat history
            else:
                st.warning("Please enter a message before sending.")
    else:
        # Display a message if the username is not entered yet
        st.warning("Please enter a username to start chatting.")

if __name__ == "__main__":
    main()
