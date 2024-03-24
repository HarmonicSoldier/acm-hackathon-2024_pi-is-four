import os
import tkinter as tk

class Question:
        def __init__(self, prompt , answer):
            self.prompt = prompt
            self.answer = answer

def display_questionaire():
    question_lines = []

    """
    Reads questions from the "Demo.txt" file and save them to questionList
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    file_path = os.path.join(current_dir, "Demo.txt")

    # Read only question lines
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














    # Function to handle
     
    # Create a temporary window to get screen dimensions
    temp_window = tk.Tk()
    screen_width = temp_window.winfo_screenwidth()
    screen_height = temp_window.winfo_screenheight()
    temp_window.destroy()  # Destroy the temporary window

    # Create a new window
    window = tk.Tk()
    window.title("Question Key")
    window.configure(bg="whitesmoke")  # Set background color to black

    # Set the window size to fit the screen
    window.geometry(f"{int(screen_width * 0.8)}x{int(screen_height * 0.8)}")

    # Create a label to display the names
    label = tk.Label(window, text="\n".join(names),
                     font=("Arial", 16), fg="dimgray", bg="whitesmoke")  # Set text color to green
    label.pack(padx=20, pady=20)

    # Entry widget to enter new name
    entry = tk.Entry(window, font=("Arial", 12), bg="whitesmoke", fg="black")
    entry.pack(padx=20, pady=(0, 10))

    # Button to add new name
    button = tk.Button(window, text="Add Name", command=add_name, bg="lightsteelblue", fg="black", font=("Arial", 12))
    button.pack(padx=20, pady=(0, 20))

    # Run the main event loop
    window.mainloop()