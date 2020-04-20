#main loop
def main():
    global str_Topic
    global str_Difficulty
    str_Topic = get_TopicChoice()
    str_Difficulty = get_DifficultyChoice()
    print("You have chosen to do", str_Difficulty, str_Topic)

#user chooses the topic
def get_TopicChoice():
    print("You are going to choose a topic for the quiz")
    bol_TopicChosen = False
    while bol_TopicChosen == False:
        try:
            print("Type 1 for Geography:")
            print("Type 2 for History:")
            int_TopicChoice = int(input("Type 3 for Maths:\n"))
            
            if int_TopicChoice == 1:
                top = "geography"
                bol_TopicChosen = True
                break
    
            if int_TopicChoice == 2:
                top = "history"
                bol_TopicChosen = True
                break

            if int_TopicChoice == 3:
                top = "maths"
                bol_TopicChosen = True
                break

            print("Incorrect input")
            print("Please try again")
                
        except ValueError:
            print("Incorrect input, please try again")

        

    return top


#user chooses a difficulty
def get_DifficultyChoice():
    print("\nYou are going to chose a Difficulty for the quiz")
    bol_DifficultyChosen = False
    while bol_DifficultyChosen == False:
        try:
            print("Type 1 for Easy:")
            print("Type 2 for medium:")
            int_DifficultyChoice = int(input("Type 3 for Hard:\n"))

            if int_DifficultyChoice == 1:
                diff = "easy"
                bol_DifficultyChosen = True
                break

            if int_DifficultyChoice == 2:
                diff = "medium"
                bol_DifficultyChosen = True
                break

            if int_DifficultyChoice == 3:
                diff = "hard"
                bol_DifficultyChosen = True
                break
                                       
            print("Incorrect input")
            print("Please try again")

        except ValueError:
            print("Incorrect input")

    return diff

main()
