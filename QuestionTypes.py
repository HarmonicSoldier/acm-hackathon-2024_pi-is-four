# Code the following:
#   1. The user1 answers 10 questions
#       a. Types of questions are determined by their respective answer format
#       b. The two main types we will be showcasing are a multiple choice and a scale (Likert?)
#           * multiple choice- generic or fictional icebreaker questions, general answers have a relation to traits/personalities
#           * scale- Likert question answers with ("Strongly Disagree," "Disagree," "Neutral," "Agree," "Strongly Agree")
#!      c. Both types will be inner classes of the parent questionClass
#   2. Answers are recorded in a key-value pair
#       a. 
#X      b. integrate string matching algorithm (fuzzy Python library?)
#X          * should both Scale and Multiple-choice answers take in inputs (char, pattern)
#X          * Each user's submission is assigned the string of characters representing either the quesNum or score <- needs revision


#if parent class takes values (prompt,answer), 
#X   then the two child class takes values (key,value)
class Question:
    def __init__(self, prompt , answer):
        self.prompt = prompt
        self.answer = answer
----------------------------------working

#Goal: read prompts and place them into the list
prompt_list = ["What is your favorite season?", ] # all prompts are pulled from the "list of questions file"

#this will be looped? 
Question(prompt_list[0])



#Goal: record user1 answers into a string to write to the "txt.file"
#   Example_Case: user1 has "A, D, B, C, D, B, A, D, C, A"
#       save string to file

# TEST DRIVER 2
i=0
overall_dict = {} # indexing (quesNum, score)

while not i == 10:
    quesNum = int(input("Enter the question number: "))     #userinput-> pull from "list of questions file" 
    score = float(input("Enter the score: "))               #Calculate user1's overall score
    
    overall_dict.update({quesNum: score})
    i += 1
    print(i)
print(overall_dict)