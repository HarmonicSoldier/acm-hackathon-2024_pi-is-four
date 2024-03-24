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
    def __init__(self, prompt , answers):
        self.prompt = prompt #string containing full question prompt for user 
        self.answer = answers #array containing strings of possible answers

    def getPrompt():
        return prompt

    def getAnswers():
    """returns array of strings containing list of possible answers"""
        return answers

    def compareAnswers(ans1, ans2):
        return (ans1 == ans2)

# Respondents will choose from a list

class MultipleChoice(Question):
"""respondents are presented with a question; respond from list of provided choices"""
    def __init__(self, prompt, answers)
        self.prompt = prompt
        self.answer = answer

    def compareAnswers(ans1, ans2):
    """ records similarity between answers. 

    Keyword arguments:
    ans1 - integer from 1 to num_questions
    ans2 - integer from 1 to num_questions
    """
       return (ans1 == ans2)


class Scale(Question):
"""respondents are presented with a statement; respond from strongly disagree to strongly agree """

    #The following are biases, which can be set between 0 and 1
    # 0 - the bias has no effect
    # 1 - the bias sets the relevant similarity scores to 1
    
    #increase similarly score between agree / strongly agree and disagree / strongly disagree pairs
    ALIGNMENT_BIAS=0.5


    def compareAnswers(ans1, ans2):
    """ records similarity between asnwers. """

    Keyword arguments:
    ans1 - integer from -2 (strongly disagree) to 2 (strongly agree)
    ans2 - integer from -2 (strongly disagree) to 2 (strongly agree)

      if (ans1 * ans2 > 0):
        bias=ALIGNMENT_BIAS
      else:
        bias=0
     
      return (1 - (1 - bias) * abs(ans1 - ans2) / 4)

def getAnsSimilarity(answerSet1, answerSet2, questionList):
   """given two arrays of answer sets, returns a measure of their similarity

   Keyword arguments:
   answerSet1: a full vector of answers, in the same order as the questionList
   answerSet2: a full vector of answers, in the same order as the questionList
   """

   difference = 0
   for i in range(len(questionList)):
       difference += (1 - questionList[i].compareAnswers(answerSet1[i], answerSet2[i])) ** 2

   return (1 - difference / len(questionList))
 
def getClosest(UserData, myUser, questionList, numUsers)
    """returns a sorted list of the most similar user
       output is an array of UIDs sorted by closeset 
    
    Keyword arguments:
    UserData - a dictionary between the following terms:
        first entry (UID) - a unique name (either numeric string or username) for each user
        second entry (answers) - an array containing answers to the first questions
    baseUser - the UID of the person to compare to 
    numUsers - only output the first numUsers users
    """
    users = UserData.keys()
    myAnswerSet = UserData[myUser]

    numUsersToCheck = len(questionList)
    if numUsers >= numUsersToCheck:
        return users

    most_similar_users = users[0:numUsers - 1]
    sorted(most_similar_users, key=lambda cand_uid: -UserData[cand_uid])

    for cand_uid in users[numUsers:numUsersToCheck - 1]:
        cand_sim = getAnsSimilarity(baseAnswerSet, UserData[cand_uid], questionList)
        for i in range(numUsers):
            if cand_sim >= getAnsSimilarity(baseAnswerSet, UserData[most_similar_users[i]], questionList):
                most_similar_users.insert(i + 1, cand_uid)
                most_similar_users = most_similar_users[0:numUsers - 1]
                break

        
#i'd strongly recommend debugging the above code    

  
#----------------------------------working


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
