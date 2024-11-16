import streamlit as st
import os
import time
import random
import string

# Directory to save chat history files
CHAT_HISTORY_DIR = 'chat_history'

# Ensure the chat history directory exists
if not os.path.exists(CHAT_HISTORY_DIR):
    os.makedirs(CHAT_HISTORY_DIR)

# Function to generate a unique file name based on current timestamp and random string
def generate_unique_filename():
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Time-based unique ID
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{timestamp}_{random_suffix}.txt"

# Function to save the chat message to a unique file
def save_message_to_file(message):
    filename = generate_unique_filename()
    file_path = os.path.join(CHAT_HISTORY_DIR, filename)
    
    # Add the message to the file
    with open(file_path, 'w') as file:
        file.write(message)

# Streamlit interface for the chat
def main():
    st.title("Anonymous Chat")

    # Display instructions
    st.write("Welcome to the anonymous chat. Type your message and hit send!")

    # Text input for user message
    user_message = st.text_input("Your message:")

    if st.button("Send"):
        if user_message:
            # Save the message to a unique file
            save_message_to_file(user_message)
            st.success("Your message has been sent!")
            st.text_area("Chat History", user_message, height=200)
            st.experimental_rerun()  # Rerun to clear input field and update the chat history
        else:
            st.warning("Please enter a message before sending.")

if __name__ == "__main__":
    main()

