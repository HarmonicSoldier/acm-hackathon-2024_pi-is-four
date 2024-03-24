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
        self.questions = questions  # list of Question objects
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
        #end of the questionnaire
        print("Questionnaire completed. Answers:", self.answers)
        self.manager.current = 'matching'
       
        
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
       
class Name:
    def __init__(self, full_name):
        self.full_name = full_name

names = [
    Name("Tom Bombadil"),
    Name("Gordon Freeman"),
    Name("Tirion Fordring"),
    Name("Jon Snow"),
    Name("Stephen Hawking"),
    Name("Aragorn Son of Arathorn"),
    Name("Sylvanas Windrunner"),
    Name("Carl Sagan")
]

def get_random_names(num_names=3):
    num_names = min(num_names, len(names))
    return random.sample(names, num_names)

class OptionsPopup(Popup):
    def __init__(self, match_name, screen_manager, **kwargs):
        super(OptionsPopup, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.match_name = match_name
        

    def open_chat(self, instance):
        # Logic to open chat with match_name
        print(f"Opening chat with {self.match_name}")
        # Switch to chat screen if it exists
        self.screen_manager.current = 'chat_screen_name'
        self.dismiss()

    def block_user(self, instance):
        # Logic to block the user
        print(f"Blocking {self.match_name}")
        # Perform blocking operation (no screen switch needed here)
        self.dismiss()
        
class MatchHubScreen(Screen):
    def __init__(self, **kwargs):
        super(MatchHubScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        #Label
        self.match_list_label = Label(text="Your Matches:")
        layout.add_widget(self.match_list_label)

        random_names = get_random_names(3)
        for name_obj in random_names:
            btn = Button(text=name_obj.full_name)
            btn.bind(on_press=self.open_options)
            layout.add_widget(btn)
            
        self.add_widget(layout)
    def open_options(self, instance):
        selected_match = instance.text
        options_popup = OptionsPopup(selected_match, self.manager)
        options_popup.open()
        
 class A_Friend_In_10_App(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BootScreen(name='boot'))
        sm.add_widget(UserScreen(name='user'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(QuestionnaireScreen(name='questionnaire'))
        sm.add_widget(MatchingBootScreen(name='matching'))
        sm.add_widget(MatchHubScreen(name='matchhub'))  
