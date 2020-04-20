global score
global pos
pos = 1

#the main loop function
def main():
    global score
    score = 0
    print("You will now be given a percentage, grade and comment about your score")
    print("Final score:", score)
    int_ScorePCTG = score / 5 * 100
    print("Final percentage:", int_ScorePCTG)
    if int_ScorePCTG == 0:
        str_Grade = "E"
        str_GradeComment = "A terrible score, how about you retry"
    if int_ScorePCTG == 20:
        str_Grade = "D"
        str_GradeComment = "A bad score, how about you retry"
    if int_ScorePCTG == 40:
        str_Grade = "C"
        str_GradeComment = "An alright score, how about you retry"
    if int_ScorePCTG == 60:
        str_Grade = "B"
        str_GradeComment = "A good score"
    if int_ScorePCTG == 80:
        str_Grade = "A"
        str_GradeComment = "A very good score"
    if int_ScorePCTG == 100:
        str_Grade = "A*"
        str_GradeComment = "An amazing score, retry with a harder difficulty"
    print("Final grade:", str_Grade)
    print(str_GradeComment)

    print("\nStoring score...")


    
    list_Results = OpenFileintoList("results")
    str_AppendMsg = " || " + str(score) + " | " + str(int_ScorePCTG) + " | " + str_Grade + " | " + str_GradeComment + " "
    list_Results[pos] = list_Results[pos] + str_AppendMsg
    
    file_Results = open("results.txt", "w")
    for number5 in range(len(list_Results)):
        file_Results.write(list_Results[number5] + "\n")
        
    file_AllScores = open("allscores.txt", "a")
    file_AllScores.write(str(score) + "\n")
    
    file_Results.close()
    file_AllScores.close()

    print("Stored")

#formats the list
def OpenFileintoList(name):
    file_ = open(name+".txt", "r")
    list_ = file_.readlines()
    list_ = [x.strip() for x in list_]
    file_.close()
    return list_

    

main()
