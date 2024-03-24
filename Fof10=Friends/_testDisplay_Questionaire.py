import os
import tkinter as tk

def display_data():
    """
    Reads names from the "Demo.txt" file and displays them in a separate window.
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    file_path = os.path.join(current_dir, "_Demo.txt")

    # Read the names from the file
    with open(file_path, "r") as file:
        data = [data.strip() for data in file.readlines()]
    return data
    

# Call the display_names function to start the program
print(display_data())
data= (display_data())

# questionnaireList should be empty first, then code reads "questionnaireList.txt" so other functions like getAnswers() work
class Question:
        def __init__(self, prompt , answer):
            self.prompt = prompt
            self.answer = answer

questionnaireList = [
    Question("What is your favorite season? \n(a) Spring\n(b) Summer\n(c) Fall\n(d) Winter\n\n", None),
    Question("What would you grab first? \n(a) Food/Water\n(b) Weapons\n(c) Pet\n(d) Book\n\n", None),
    Question("What is your ideal dream home? \n(a) Million-dollar penthouse\n(b) Modern Tropical Mansion\n(c) United Kingdom stately home\n(d) Winter Cabin\n\n", None)
    ]
    
def record_answers(questionnaireList):
    answers = []
    filter = True
    for question in questionnaireList:
        while filter == True:
            selection = input(question.prompt).lower().strip()
            if selection in ["a", "b", "c", "d"]:
                answers.append(selection)
                break
            else:
                print("Invalid input. Please enter a, b, c, d\n\n")
    return answers
    
    #write to file?
user1_answers = record_answers(questionnaireList)
    
print(user1_answers)