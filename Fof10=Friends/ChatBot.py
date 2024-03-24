import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
from friend_names import get_random_name
from AddFriend import AddFriendWindow  # Import AddFriendWindow class

def chat_bot(bot_name):
    """
    A simple chatbot that responds to user input.
    """
    conversation_history = {}  # To store conversation history

    # List of random countries
    countries = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Japan", "Brazil", "India", "China"]

    def bot_respond(event=None):
        user_input = entry.get().lower().strip()
        if user_input:
            conversation_area.configure(state="normal")
            conversation_area.insert(tk.END, f"You: {user_input}\n\n", "user")
            response = generate_response(user_input)
            conversation_area.insert(tk.END, f"{bot_name}: {response}\n\n", "bot")
            conversation_history.setdefault(user_input, []).append(response)  # Remember conversation history
            entry.delete(0, tk.END)
            entry.focus()
            conversation_area.configure(state="disabled")

    def generate_response(user_input):
        greetings = ["hello", "hi", "hey"]
        farewells = ["bye", "goodbye"]
        thank_you = ["thank", "thanks"]
        questions = [
            "how are you", "whats your favorite color", "hows the weather", "how old are you", 
            "whats your name", "what kind of music do you like", "where are you from"
        ]
        
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
            return random.choice([
                "What do you like to do in your free time?",
                "Tell me about your favorite vacation.",
                "What's the most interesting book you've read recently?",
                "Do you have any pets?",
                "What's your favorite hobby?",
                "Tell me about your family.",
                "What's the best movie you've seen lately?",
                "What's your dream vacation destination?",
                "What do you enjoy doing on weekends?",
                "What's your favorite food?",
                "Tell me about your favorite childhood memory.",
                "What's the last concert you went to?",
                "Do you prefer coffee or tea?",
                "What's the last TV show you binge-watched?",
                "Tell me about your dream job.",
                "What's your favorite sport?",
                "What's your favorite thing about yourself?",
                "What's your biggest achievement?",
                "Tell me about your favorite restaurant.",
                "What's the best gift you've ever received?",
                "What's your favorite season?",
                "What's your favorite quote?",
                "Tell me about your best friend.",
                "What's your go-to karaoke song?"
            ])

    def generate_question_response(user_input):
        if "how are you" in user_input:
            return random.choice(["I'm doing well, thank you!", "I'm fine, how about you?", "Pretty good, thanks for asking!"])
        elif "whats your favorite color" in user_input:
            colors = ["red", "blue", "green", "yellow", "purple", "orange"]
            return f"My favorite color is {random.choice(colors).capitalize()}!"
        elif "what kind of music do you like" in user_input:
            music_genres = ["pop", "rock", "hip hop", "jazz", "classical", "electronic", "country"]
            return f"I enjoy listening to {random.choice(music_genres)} music!"
        elif any(word in user_input for word in ["hows the weather", "what's the weather like", "whats the weather doing"]):
            weather = ["stormy", "sunny", "rainy", "windy", "hot", "cold", "cloudy", "snowy"]
            return f"It is {random.choice(weather)} outside!"
        elif "how old are you" in user_input:
            return f"I am {random.randint(18, 60)} years old!"
        elif "whats your name" in user_input:
            return f"My name is {bot_name}!"
        elif "where are you from" in user_input:
            return f"I am from {random.choice(countries)}."
        else:
            return random.choice(["I'm not sure I understand.", "Could you tell me more?", "That's interesting."])

    def send_friend_request():
        add_friend_window = AddFriendWindow(window, bot_name)

    window = tk.Tk()
    window.title(f"{bot_name} - Chatbot")
    window.configure(bg="lightblue")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = int(screen_width * 0.5)  # Half of the screen width
    window_height = int(screen_height * 0.5)  # Half of the screen height
    window.geometry(f"{window_width}x{window_height}+{screen_width//2 - window_width//2}+{screen_height//2 - window_height//2}")

    conversation_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10, bg="white")
    conversation_area.pack(expand=True, fill="both", padx=20, pady=20)
    conversation_area.configure(state="disabled")

    # Function to open AddFriendWindow upon clicking the name
    def open_add_friend_window(event):
        send_friend_request()

    # Configure tag_bind to open AddFriendWindow upon clicking the name
    conversation_area.tag_config("bot", foreground="red", underline=True)
    conversation_area.tag_bind("bot", "<Button-1>", open_add_friend_window)

    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(fill="x", padx=20, pady=(0, 20))
    entry.bind("<Return>", bot_respond)

    entry.focus_set()  # Set focus to the entry widget immediately upon opening

    send_button = tk.Button(window, text="Send", command=bot_respond)
    send_button.pack(padx=20, pady=(0, 20))

    # Place "Created by π=4" label in the bottom right corner
    created_by_label = tk.Label(window, text="Created by π=4", bg="lightblue")
    created_by_label.place(relx=1.0, rely=1.0, anchor="se")

    window.mainloop()

if __name__ == "__main__":
    bot_name = get_random_name()
    chat_bot(bot_name)
