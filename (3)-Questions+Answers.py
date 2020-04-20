import random
global score
global Difficulty
global Topic

#for testing purposes, in proper use, would not be in program
Difficulty = "medium"
Topic = "geography"

#the main function that starts everything
def main():
    global score
    score = 0
    int_QuestionNumber = 1
    print("You will now do the quiz")
    for number1 in range(5):
        list_QuestionBlock = get_QuestionBlock(int_QuestionNumber)
        askQuestion(list_QuestionBlock)
        int_QuestionNumber += 1

    print("You have finished the quiz with a score of", score)
    
    

#creates a list containing question and multiple choice answers
def get_QuestionBlock(qnumber):
    str_Filename = "_"+Topic + "questions.txt"
    file_ = open(str_Filename, "r")
    for number2 in range(qnumber):
        list_ = []
        for number3 in range(6):
            list_.append(file_.readline())
            list_ = [y.strip() for y in list_]

    file_.close()

    return list_


#asks all the questions using the list, requests an answer, and checks it
def askQuestion(qblock):
    global score
    print(qblock[0])
    if Difficulty == "easy":
        int_MultipleChoiceAns = 2
        randomnum1_2 = random.randint(1,int_MultipleChoiceAns)
        if randomnum1_2 == 1:
            print("Type 1 for", qblock[1] + ":")
            int_AnswerGuess = int(input("Type 2 for " + qblock[2] + ":\n"))
            int_CorrectAnswer = 1
            
        if randomnum1_2 == 2:
            print("Type 1 for", qblock[2] + ":")
            int_AnswerGuess = int(input("Type 2 for " + qblock[1] + ":\n"))
            int_CorrectAnswer = 2


    if Difficulty == "medium":
        int_MultipleChoiceAns = 3
        randomnum1_3 = random.randint(1,int_MultipleChoiceAns)
        if randomnum1_3 == 1:
            print("Type 1 for", qblock[1] + ":")
            print("Type 2 for", qblock[2] + ":")
            int_AnswerGuess = int(input("Type 3 for " + qblock[3] + ":\n"))
            int_CorrectAnswer = 1
            
        if randomnum1_3 == 2:
            print("Type 1 for", qblock[2] + ":")
            print("Type 2 for", qblock[3] + ":")
            int_AnswerGuess = int(input("Type 3 for " + qblock[1] + ":\n"))
            int_CorrectAnswer = 3
            
        if randomnum1_3 == 3:
            print("Type 1 for", qblock[3] + ":")
            print("Type 2 for", qblock[1] + ":")
            int_AnswerGuess = int(input("Type 3 for " + qblock[2] + ":\n"))
            int_CorrectAnswer = 2

        
    if Difficulty == "hard":
        int_MultipleChoiceAns = 4
        randomnum1_4 = random.randint(1,int_MultipleChoiceAns)
        if randomnum1_4 == 1:
            print("Type 1 for", qblock[1] + ":")
            print("Type 2 for", qblock[2] + ":")
            print("Type 3 for", qblock[3] + ":")
            int_AnswerGuess = int(input("Type 4 for " + qblock[4] + ":\n"))
            int_CorrectAnswer = 1

        if randomnum1_4 == 2:
            print("Type 1 for", qblock[2] + ":")
            print("Type 2 for", qblock[3] + ":")
            print("Type 3 for", qblock[4] + ":")
            int_AnswerGuess = int(input("Type 4 for " + qblock[1] + ":\n"))
            int_CorrectAnswer = 4

        if randomnum1_4 == 3:
            print("Type 1 for", qblock[3] + ":")
            print("Type 2 for", qblock[4] + ":")
            print("Type 3 for", qblock[1] + ":")
            int_AnswerGuess = int(input("Type 4 for " + qblock[2] + ":\n"))
            int_CorrectAnswer = 3

        if randomnum1_4 == 4:
            print("Type 1 for", qblock[4] + ":")
            print("Type 2 for", qblock[1] + ":")
            print("Type 3 for", qblock[2] + ":")
            int_AnswerGuess = int(input("Type 4 for " + qblock[3] + ":\n"))
            int_CorrectAnswer = 2
            
    if int_AnswerGuess == int_CorrectAnswer:
        print("Correct answer")
        score += 1
        print("Your score is now", score, "\n")
    else:
        print("Incorrect answer")
        print("The correct answer was", qblock[1])
        print("Your score is still", score, "\n")
        

#formats the list
def OpenFileintoList(name):
    file_ = open(name+".txt", "r")
    list_ = file_.readlines()
    list_ = [x.strip() for x in list_]
    file_.close()
    return list_




main()
