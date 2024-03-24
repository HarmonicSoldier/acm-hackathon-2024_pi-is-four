##Ignore what's commented out, that's stuff I'm still working on getting into the new format with the screen manager, 
##will update as I complete each screen - Max
## Hackathon Project A Friend in 10 - Matt, Max, Noah, Zach


from cgitb import text
from typing import Self
from kivy.app import App
from kivy.base import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollViewApp
import random
import os
from kivy.uix.screenmanager import Screen, ScreenManager


class BootScreen(Screen):
    def __init__(self, **kwargs):
        super(BootScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        # Set up the background color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color to white
            self.rect = Rectangle(pos=self.pos, size=self.size)
                
        # Update the rectangle size every time BootScreen's size changes
        self.bind(size=self._update_rect, pos=self._update_rect)
            
        self.size_hint = (None, None)
        self.size = (300, 200)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Welcome Label
        Welcome_Label = Label(text="Welcome to Find a Friend in 10", size_hint_y=None, height=40, color=(1, 0, 0, 1))
        self.add_widget(Welcome_Label)

        # Update progress bar
        self.progress1_event = Clock.schedule_interval(self.update_progress1, 0.05)

    def update_progress1(self, dt):
        if self.progress_bar1.value < 100:
            self.progress_bar1.value += 1
        else:
            Clock.unschedule(self.progress1_event)
            self.manager.current = 'user'
            
class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Username Label
        layout.add_widget(Label(text='Enter your username:'))

        # Username Text Input
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        # Submit Button
        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.on_submit)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def on_submit(self, instance):
        username = self.username_input.text
        print(f"Username: {username}")
        self.manager.current = 'main'

    def switch_to_main_screen(self):
        self.manager.current = 'main'

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        questionnaire_button = Button(text='Answer 10 Questions')
        questionnaire_button.bind(on_press=self.go_to_questionnaire)

        inbox_button = Button(text='Return to Inbox')
        inbox_button.bind(on_press=self.go_to_inbox)

        layout.add_widget(questionnaire_button)
        layout.add_widget(inbox_button)

        self.add_widget(layout)

    def go_to_questionnaire(self, instance):
        self.manager.current = 'questionnaire'

    def go_to_inbox(self, instance):
        self.manager.current = 'inbox'
        
class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options

questions = [
    Question("If you were gearing up for a zombie apocalypse and could only choose one resource to have in abundance, what would you go for?",
             ["Food/Water", "Weapons", "Pets", "Books"]),
    Question("What is your favorite season?", ["Spring", "Summer", "Fall", "Winter"]),
    Question("What is your ideal dream home?",["Million-dollar penthouse","Modern Tropical Mansion","United Kingdom stately home","Winter Hunting Cabin"]),
    Question("What is your top vacation plan?", ["Climb Mt. Everest", "Visit the pyramids of Giza", "Visit an amusement park", "Vist a great beach"]),
    Question("What is your favorite TV-show-genre?", ["Comedy", "Action/Adventure", "Drama", "Documentary"]),
    Question("What is the best way to spend a lazy Sunday afternoon", ["Reading a book", "Binge watching a TV show", "Cooking/baking", "Nap time!"]),
    Question("If you could visit any fictional world, where would you go?", ["Hogwarts", "Middle Earth", "Star Wars", "Star Trek"]),
    Question("If you could explore the world using only one mode of transport for the rest of your life, which would you choose?", ["Land - traversing continents by road, rail, or foot", "Sea - sailing the oceans aboard a ship or yacht", "Air - soaring through the skies in a plane or hot air balloon", "Underwater - diving into the depths to discover the myseries of the sea"]),
    Question("If you could instantly become fluent in one language other than your native tongue, which would you choose?", ["Spanish", "Japenese", "French", "Mandarin Chinese"])             
]

class QuestionnaireScreen(Screen):
    def __init__(self, **kwargs):
        super(QuestionnaireScreen, self).__init__(**kwargs)
        self.questions = questions  # Assuming 'questions' is a list of Question objects
        self.current_question_index = 0
        self.answers = []
        self.display_question()

    def display_question(self):
        self.clear_widgets()

        # Check if there are still questions left
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.add_widget(Label(text=question.text))

            # Create buttons for each answer option
            for index, option in enumerate(question.options, start=1):
                btn = Button(text=f"Answer {chr(64 + index)}: {option}")
                btn.bind(on_press=self.record_answer)
                self.add_widget(btn)
        else:
            self.finish_questionnaire()

    def record_answer(self, instance):
        # Store the answer and move to the next question
        self.answers.append(instance.text)
        self.current_question_index += 1
        self.display_question()

    def finish_questionnaire(self):
        # Handle the end of the questionnaire
        print("Questionnaire completed. Answers:", self.answers)
        # switch to match loading screen

class MatchingBootScreen(Screen):
    def __init__(self, **kwargs):
        super(MatchingBootScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Matching Label
        Matching_Label = Label(text="Loading your matches!", size_hint_y=None, height=40, color=(1, 0, 0, 1))
        self.add_widget(Matching_Label)
        
        # Initialize and add ProgressBar
        self.progress_bar2 = ProgressBar(value=0, max=100)
        self.add_widget(self.progress_bar2)

        # Update progress bar
        self.progress2_event = Clock.schedule_interval(self.update_progress2, 0.05)

def update_progress2(self, dt):
    if self.progress_bar2.value < 100:
        self.progress_bar2.value += 1
    else:
        Clock.unschedule(self.progress2_event)
        self.manager.current = 'match'
        
# # Set up the screen manager
# class MyApplication(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(LoggedInScreen(name='loggedin'))
#         sm.add_widget(QuestionnaireScreen(name='questionnaire'))
#         return sm


#         ##Generates first question
#     # last Question:
#     # def __init__(self, prompt, answer):
#     #     self.prompt = prompt
#     #     self.answer = answer

# def read_questions():
#     question_lines = []
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(current_dir, "Demo.txt")

#     with open(file_path, "r") as file:
#         for line in file:
#             if line.strip().startswith(('1.', '2.', '3.')):
#                 question_lines.append(line.strip())
#     return question_lines

# class QuestionnaireScreen(BoxLayout):
#     def __init__(self, **kwargs):
#         super(QuestionnaireScreen, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.padding = [10, 10, 10, 10]
#         self.spacing = 10

#         self.questions = [Question(q, None) for q in read_questions()]
#         self.current_question_index = 0
#         self.answers = []

#         # Question Label
#         self.question_label = Label(text=self.questions[0].prompt, size_hint_y=None, height=60)
#         self.add_widget(self.question_label)

#         # Answer Input
#         self.answer_input = TextInput(multiline=False, size_hint_y=None, height=40)
#         self.add_widget(self.answer_input)

#         # Next Question Button
#         self.next_button = Button(text='Next Question', size_hint_y=None, height=50)
#         self.next_button.bind(on_press=self.record_answer)
#         self.add_widget(self.next_button)


#     def record_answer(self, instance):
#         answer = self.answer_input.text.lower().strip()
#         if answer in ["a", "b", "c", "d"]:
#             self.answers.append(answer)
#             self.next_question()
#         else:
#             self.question_label.text = "Invalid input. Please enter a, b, c, d\n\n" + self.question_label.text

#     def next_question(self):
#         self.current_question_index += 1
#         if self.current_question_index < len(self.questions):
#             self.question_label.text = self.questions[self.current_question_index].prompt
#             self.answer_input.text = ''
#         else:
#             self.question_label.text = "Questionnaire completed."
#             self.answer_input.disabled = True
#             self.next_button.disabled = True
#             print(self.answers)  # Handle the answers as needed
            
# ## Matchhub
# def get_random_names(num_names=3):
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(current_dir, "FriendNames.txt")
#     with open(file_path, "r") as file:
#         names = [name.strip() for name in file.readlines()]
#     return random.sample(names, num_names)

# class MatchHubScreen(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(orientation='vertical', **kwargs)

#         self.matches = get_random_names()

#         self.match_list_label = Label(text="Your Matches:", size_hint_y=0.1)
#         self.add_widget(self.match_list_label)

#         self.match_list = ListView(item_strings=self.matches, size_hint_y=0.7)
#         self.add_widget(self.match_list)

#         self.answer_questions_button = Button(text="Answer More Questions", on_press=self.answer_questions, size_hint_y=0.1)
#         self.add_widget(self.answer_questions_button)

#         self.block_button = Button(text="Block", on_press=self.block_user, size_hint_y=0.1)
#         self.add_widget(self.block_button)

#         self.credit_label = Label(text="Created by Π=4", size_hint_y=0.1)
#         self.add_widget(self.credit_label)

#     def answer_questions(self, instance):
#         print("Answering more questions...")

#     def block_user(self, instance):
#         selected_match = self.match_list.adapter.selection[0].text if self.match_list.adapter.selection else None
#         if selected_match:
#             # Confirmation popup
#             content = ConfirmPopup()
#             self.popup = Popup(title="Confirmation", content=content, size_hint=(0.5, 0.5))
#             content.ids.yes.bind(on_press=lambda x: self.remove_match(selected_match))
#             content.ids.no.bind(on_press=self.popup.dismiss)
#             self.popup.open()

#     def remove_match(self, match_name):
#         if match_name in self.matches:
#             self.matches.remove(match_name)
#             self.match_list.item_strings = self.matches
#             self.popup.dismiss()

#     def open_chat(self, instance):
#         selected_match = instance.text
#         chat_bot(selected_match)

# class ConfirmPopup(FloatLayout):
#     pass

# class MatchHubApp(App):
#     def build(self):
#         return MatchHubScreen()            
# ## At end of questions generates preparing matches loading screen
# class MatchLoadingScreen(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

#         self.loading_label = Label(text="Loading Matches...", size_hint=(1, 0.2))
#         self.add_widget(self.loading_label)

#         self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.2))
#         self.add_widget(self.progress_bar)

#         self.go_to_matches_button = Button(text="Go To Matches", size_hint=(1, 0.2), disabled=True)
#         self.go_to_matches_button.bind(on_press=self.go_to_matches)
#         self.add_widget(self.go_to_matches_button)

#         self.progress = 0
#         Clock.schedule_interval(self.load_matches, 0.1)

#     def load_matches(self, dt):
#         self.progress += 5
#         if self.progress > 100:
#             self.progress = 100
#             Clock.unschedule(self.load_matches)
#             self.loading_label.text = "Matches loaded successfully!"
#             self.go_to_matches_button.disabled = False
#         self.progress_bar.value = self.progress

#     def go_to_matches(self, instance):
#         self.clear_widgets()
#         # Add the MatchHub screen here
#         # Ensure MatchHub is properly converted to work with Kivy
#         self.add_widget(Label(text="Match Hub Screen"))  # Placeholder for MatchHub

# ## Congradulations animation screen with options to start chat with matched user or answer another 10 questions
    
# ## Chatbot
# class ChatBotScreen(BoxLayout):
#     def __init__(self, bot_name, **kwargs):
#         super().__init__(orientation='vertical', **kwargs)
#         self.bot_name = bot_name
#         self.conversation_history = {}

#         self.conversation_area = TextInput(readonly=True, size_hint_y=0.8)
#         self.add_widget(self.conversation_area)

#         self.entry = TextInput(size_hint_y=0.1, multiline=False)
#         self.entry.bind(on_text_validate=self.bot_respond)
#         self.add_widget(self.entry)

#         self.send_button = Button(text="Send", size_hint_y=0.1)
#         self.send_button.bind(on_press=self.bot_respond)
#         self.add_widget(self.send_button)

#     def bot_respond(self, instance):
#         user_input = self.entry.text.lower().strip()
#         if user_input:
#             self.conversation_area.text += f"You: {user_input}\n"
#             response = self.generate_response(user_input)
#             self.conversation_area.text += f"{self.bot_name}: {response}\n"
#             self.conversation_history.setdefault(user_input, []).append(response)
#             self.entry.text = ''
    
# ## Send friend Request to matches
# class ConfirmPopup(FloatLayout):
#     pass

# class AddFriendWindow(BoxLayout):
#     def __init__(self, friend_name, **kwargs):
#         super().__init__(orientation='vertical', **kwargs)
#         self.friend_name = friend_name

#         self.label = Label(text=f"Options for {self.friend_name}", font_size='20sp')
#         self.add_widget(self.label)

#         self.send_button = Button(text="Send Friend Request", on_release=self.send_friend_request)
#         self.add_widget(self.send_button)

#         self.block_button = Button(text="Block", on_release=self.confirm_block_user)
#         self.add_widget(self.block_button)

#     def send_friend_request(self, instance):
#         self.label.text = "Friend Request Sent"
#         self.send_button.disabled = True

#     def confirm_block_user(self, instance):
#         content = ConfirmPopup()
#         self.popup = Popup(title="Confirmation", content=content, size_hint=(0.5, 0.5))
#         content.ids.yes.bind(on_release=self.block_user)
#         content.ids.no.bind(on_release=self.popup.dismiss)
#         self.popup.open()

#     def block_user(self, instance):
#         self.label.text = "User Blocked"
#         self.block_button.disabled = True
#         self.popup.dismiss()
        

# class A_Friend_In_10_App(App):
#     def build(self):
#         bootup = BootScreen
# if __name__=='__main__':
#     app = A_Friend_in_10_App()
#     app.run()
