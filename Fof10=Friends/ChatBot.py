import tkinter as tk
from tkinter import scrolledtext
import random
from friend_names import get_random_name

def chat_bot(bot_name):
    """
    A simple chatbot that responds to user input.
    """
    conversation_history = []  # To store conversation history

    # List of random countries
    countries = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Japan", "Brazil", "India", "China"]

    def bot_respond(event=None):  # Modified to accept an event parameter for Enter key
        user_input = entry.get().lower().strip()  # Convert user input to lowercase and remove leading/trailing spaces
        if user_input:
            conversation_area.configure(state="normal")  # Enable conversation area for editing
            conversation_area.insert(tk.END, f"You: {user_input}\n\n", "user")  # Display user's message
            response = generate_response(user_input)  # Generate response based on user input
            conversation_area.insert(tk.END, f"{bot_name}: {response}\n\n", "bot")  # Display bot's response
            conversation_history.append((user_input, response))  # Store the conversation in history
            entry.delete(0, tk.END)
            entry.focus()  # Focus on the entry box after responding
            conversation_area.configure(state="disabled")  # Disable conversation area for editing

    # Function to generate bot responses
    def generate_response(user_input):
        # Define some basic response patterns
        greetings = ["hello", "hi", "hey"]
        farewells = ["bye", "goodbye"]
        thank_you = ["thank", "thanks"]
        questions = ["how are you", "what's your favorite color", "how's the weather", "how old are you", "what's your name", "what kind of music do you like", "where are you from"]
        
        # Check user input for greetings, farewells, thank you messages, and questions
        if any(word in user_input for word in greetings):
            response = random.choice(["Hello!", "Hi there!", "Hey!"])
            if response == "Hello!":
                response += " How are you doing today?"
            return response
        elif any(word in user_input for word in farewells):
            return random.choice(["Goodbye!", "See you later!", "Bye!"])
        elif any(word in user_input for word in thank_you):
            return random.choice(["You're welcome!", "No problem!", "Anytime!"])
        elif any(word in user_input for word in questions):
            return generate_question_response(user_input)
        else:
            # If none of the predefined patterns match, generate a generic response
            return random.choice(["I'm not sure I understand.", "Could you tell me more?", "That's interesting."])

    # Function to generate responses for specific questions
    def generate_question_response(user_input):
        if "how are you" in user_input:
            return random.choice(["I'm doing well, thank you!", "I'm fine, how about you?", "Pretty good, thanks for asking!"])
        elif "what's your favorite color" in user_input:
            colors = ["red", "blue", "green", "yellow", "purple", "orange"]
            return f"My favorite color is {random.choice(colors).capitalize()}!"
        elif "what kind of music do you like" in user_input:
            music_genres = ["pop", "rock", "hip hop", "jazz", "classical", "electronic", "country"]
            return f"I enjoy listening to {random.choice(music_genres)} music!"
        elif "how's the weather" in user_input:
            weather = ["stormy", "sunny", "rainy", "windy", "hot", "cold", "cloudy", "snowy"]
            return f"It is {random.choice(weather)} outside!"
        elif "how old are you" in user_input:
            return f"I am {random.randint(18, 50)} years old!"
        elif "what's your name" in user_input:
            return f"My name is {bot_name}! How can I assist you today?"
        elif "where are you from" in user_input:
            return f"I am from {random.choice(countries)}."
        else:
            return random.choice(["I'm not sure I understand.", "Could you tell me more?", "That's interesting."])

    # Create a new window for the chatbot
    window = tk.Tk()
    window.title(f"{bot_name} - Chatbot")
    window.configure(bg="lightblue")  # Set background color to light blue

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window size to fit the screen
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.8)
    window.geometry(f"{window_width}x{window_height}+{screen_width//2 - window_width//2}+{screen_height//2 - window_height//2}")

    # Conversation area to display messages
    conversation_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, bg="white")  # Set message area background to white
    conversation_area.pack(expand=True, fill="both", padx=20, pady=20)
    conversation_area.configure(state="disabled")  # Make conversation area read-only

    # Entry widget for user input
    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(fill="x", padx=20, pady=(0, 20))
    entry.bind("<Return>", bot_respond)  # Bind Enter key to bot_respond function
    entry.focus_set()  # Set focus to the entry box

    # Button to send user input
    send_button = tk.Button(window, text="Send", command=bot_respond)
    send_button.pack(padx=20, pady=(0, 20))

    # Define message tags for different colors
    conversation_area.tag_config("user", foreground="green")  # User messages in green
    conversation_area.tag_config("bot", foreground="red")  # Bot messages in red

    # Run the main event loop
    window.mainloop()

if __name__ == "__main__":
    bot_name = get_random_name()
    chat_bot(bot_name)
