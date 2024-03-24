import os
import tkinter as tk

def display_questionaire():
    
    class Question:
        def __init__(self, prompt , answer):
            self.prompt = prompt
            self.answer = answer
    
    # questionList should be empty first, then code reads "QuestionList.txt" so other functions like getAnswers() work
    questionList = [
        Question("What is your favorite season? \n(a) Spring\n(b) Summer\n(c) Fall\n(d) Winter\n\n", None),
        Question("What would you grab first? \n(a) Food/Water\n(b) Weapons\n(c) Pet\n(d) Book\n\n", None),
        Question("What is your ideal dream home? \n(a) Million-dollar penthouse\n(b) Modern Tropical Mansion\n(c) United Kingdom stately home\n(d) Winter Cabin\n\n", None)
        ]
    
    def record_answers(questionList):
        answers = []
        filter = True
        for question in questionList:
            while filter == True:
                selection = input(question.prompt).lower().strip()
                if selection in ["a", "b", "c", "d"]:
                    answers.append(selection)
                    break
                else:
                    print("Invalid input. Please enter a, b, c, d\n\n")
        return answers
    
    #write to file?
    user1_answers = record_answers(questionList)
    
    print(user1_answers)