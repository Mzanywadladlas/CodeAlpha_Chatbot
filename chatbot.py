# chatbot.py
# ------------------------------
import requests
from datetime import datetime

# Function: write to chat log
def log_message(sender, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {sender}: {message}\n")

# Function: get joke from internet API
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return data["setup"] + " - " + data["punchline"]

# Function: chatbot replies
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "help":
        return """
I can:
1. Tell a joke (type: joke)
2. Explain chatbots (type: chatbot)
3. Exit (type: exit)
"""

    elif user_input == "chatbot":
        return "A chatbot is a program that talks with users using text or voice."

    elif user_input == "joke":
        return get_joke()

    elif user_input == "hi":
        return "Hello! How can I help you?"
    
    elif user_input == "how are you":
        return "I'm doing great! Thanks for asking."
    
    elif user_input == "what is your name?":
        return "I am CodeAlpha Bot."

    elif user_input == "bye":
        return "Goodbye! Have a nice day"

    else:
        return "I don't understand. Type 'help'."

# ------------------------------
# Startup Menu
print("🤖 Welcome to Smart Chatbot")
print("Type 'help' to see options\n")

# Chat loop
while True:
    user = input("You: ")

    # Log user message
    log_message("You", user)

    if user.lower() == "exit":
        bot_reply = "Goodbye 👋"
        print("Bot:", bot_reply)
        log_message("Bot", bot_reply)
        break

    reply = chatbot_response(user)

    # Log bot reply
    log_message("Bot", reply)

    print("Bot:", reply)