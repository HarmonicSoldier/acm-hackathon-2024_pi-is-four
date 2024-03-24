class Question:
    def __init__(self, prompt, answers):
        self.prompt = prompt    #string containing full question prompt for user 
        self.answers = answers  #array containing strings of possible answers

    def getPrompt(self):
        return self.prompt

    def getAnswers(self):
    #"""returns array of strings containing list of possible answers"""
        return self.answers

    def compareAnswers(self, ans1, ans2):
        return ans1 == ans2


class MultipleChoice(Question):
    def __init__(self, prompt, answers):
        super().__init__(prompt, answers)

    def compareAnswers(self, ans1, ans2):
    #""" records similarity between answers. 

    # #Keyword arguments:
    #ans1 - integer from 1 to num_questions
    #ans2 - integer from 1 to num_questions
    #"""
        return ans1 == ans2


def getAnsSimilarity(answerSet1, answerSet2, questionList):
    #"""given two arrays of answer sets, returns a measure of their similarity

    #Keyword arguments: 
    #answerSet1: a full vector of answers, in the same order as the questionList
    #answerSet2: a full vector of answers, in the same order as the questionList
    #"""
    difference = 0
    for i in range(len(questionList)):
        difference += (1 - questionList[i].compareAnswers(answerSet1[i], answerSet2[i])) ** 2

    return (1 - difference / len(questionList))

def getClosest(UserData, myUser, questionList, numUsers):
    #"""returns a sorted list of the most similar user
    #   output is an array of UIDs sorted by closeset 
    
    #Keyword arguments:
    #UserData - a dictionary between the following terms:
    #    first entry (UID) - a unique name (either numeric string or username) for each user
    #    second entry (answers) - an array containing answers to the first questions
    #baseUser - the UID of the person to compare to 
    #numUsers - only output the first numUsers users
    #"""
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


# TEST DRIVER 1
questionList = [
    Question("1. What is your favorite season? \n(a) Spring\n(b) Summer\n(c) Fall\n(d) Winter\n\n", None),
    Question("2. What would you grab first? \n(a) Food/Water\n(b) Weapons\n(c) Pet\n(d) Book\n\n", None),
    Question("3. What is your ideal dream home? \n(a) Million-dollar penthouse\n(b) Modern Tropical Mansion\n(c) United Kingdom stately home\n(d) Winter Cabin\n\n", None)
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

user1_answers = record_answers(questionList)

print(user1_answers)

user2_answers = record_answers(questionList)

print(user2_answers)

print(getAnsSimilarity(user1_answers, user2_answers, questionList))