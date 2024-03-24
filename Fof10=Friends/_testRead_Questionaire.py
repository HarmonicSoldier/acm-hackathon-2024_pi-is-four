import os

class Question:
        def __init__(self, prompt , answer):
            self.prompt = prompt
            self.answer = answer
            
question_lines = []

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(current_dir, "Demo.txt")

# Read the names from the file
with open(file_path, "r") as file:
    for line in file:
        if line.strip().startswith(('1.', '2.', '3.')):
            question_lines.append(line.strip())
for question in question_lines:
    print(question)#module test
        
print(question_lines)#module test
    
   
questionList = [
    Question(question_lines[0], None),
    Question(question_lines[1], None),
    Question(question_lines[2], None)
    ]

#GUI entry for user input    
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

# Calculate compatibility by using the functions?
user1_answers = record_answers(questionList)#module test
    
print(user1_answers)#module test