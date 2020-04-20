#Welcomes the user to the quiz and explains what will happen
def welcome():
    print("Welcome to Kiran's quiz")
    print("Firstly, you will sign in/sign up")
    print("Then you will chose a difficulty and topic e.g. medium geography")
    print("You will complete the multiple choice quiz and at the end recieve your result")
    input("Press enter to continue\n")
    SignInorUp()



#Asks the user if they need to sign in or sign up
def SignInorUp():
    print("You will now be given the choice to either sign in or sign up")
    bol_SignInorUpChoice= False
    while bol_SignInorUpChoice == False:
        try:
            int_SignInorUpValue = int(input("Type '1' to sign in, or '2' to sign up:\n"))
        
            if int_SignInorUpValue == 1:
                SignIn()
                bol_SignInorUpChoice = True
                break
            if int_SignInorUpValue == 2:
                SignUp()
                bol_SignInorUpChoice = True
                break
            else:
                print("Incorrect input, please try agains")
        except ValueError:
            print("Invalid input, please try again")


#Signs the user in
def SignIn():
    global pos
    pos = CheckUsername()
    CheckPassword(pos)
    print("Signed in")
    
#Works out the position the username is in
def CheckUsername():
    str_UsernameGuess = input("Enter your username in the correct format e.g. Kir15, and the correct capital letters:\n")
    list_Usernames = OpenFileintoList("usernames")
    bol_UsernameinList = False
    while bol_UsernameinList == False:
        for pos in range(len(list_Usernames)):
            if str_UsernameGuess == list_Usernames[pos]:
                print("Username found")
                bol_UsernameinList = True
                break

        if bol_UsernameinList == False:
            print("Your username is not valid")
            print("Please retry")
            CheckUsername()
            break
                             
    return pos

#Uses the position the username is in to get the user to input the correct password
def CheckPassword(position):
        
    list_Passwords = OpenFileintoList("passwords")
    str_PasswordGuess = input("Enter your password (With correct case):\n")
    if str_PasswordGuess == list_Passwords[position]:
        print("Password found, logged in")
    else:
        print("Incorrect password, please retry")
        CheckPassword(position)

#Opens the file and reads it into a list, without \n's
def OpenFileintoList(name):
    file_ = open("dbase_"+name+".txt", "r")
    list_ = file_.readlines()
    list_ = [x.strip() for x in list_]
    file_.close()
    return list_

#Signs the user up
def SignUp():
    global str_Username
    global int_UserAge
    list_Usernames = OpenFileintoList("usernames")
    Get_Username()
    str_UserUsername = str_UserFname[:3] + str(int_UserAge)
    bol_UserUsernameFinal = False
    while bol_UserUsernameFinal == False:
        if str_UserUsername in list_Usernames:
            print("Your username is currently in use")
            int_UserAge += 1
            str_UserUsername = str_UserFname[:3] + str(int_UserAge)
        else:
            print("Your username is", str_UserUsername)
            str_Username = str_UserUsername
            bol_UserUsernameFinal = True

    Get_Password()

    file_usernames = open("dbase_usernames.txt", "a")
    file_passwords = open("dbase_passwords.txt", "a")
    file_usernames.write(str_Username + "\n")
    file_passwords.write(str_UserPassword + "\n")
    file_usernames.close()
    file_passwords.close()
    print("Added to database")


#creates a valid username, then is stored
def Get_Username():
    global str_UserFname
    global int_UserAge
    str_UserFname = input("Please enter your first name:\n")
    str_UserSname = input("Please enter your surname:\n")
    bol_AgeEntered = False
    while bol_AgeEntered == False:
        try:
            int_UserAge = int(input("Please enter your age:\n"))
            bol_AgeEntered = True
        except ValueError:
            print("Invalid input, please try again")
    print("Your firstname is", str_UserFname)
    print("Your surname is", str_UserSname)
    print("And your age is", int_UserAge)
    str_ChangeUserInfo = input("Type 'change' to edit your infomation otherwise press enter to continue\n")
    if str_ChangeUserInfo == "change":
        Get_Username()

#user creates and repeats a password, then is stored
def Get_Password():
    global str_UserPassword
    bol_UserPasswordMatch = False
    while bol_UserPasswordMatch == False:
        str_UserPassword = input("Please enter a password for the account " + str_Username + ":\n")
        str_UserPasswordRepeat = input("Please re-enter your password to confirm it:\n")
        if str_UserPassword == str_UserPasswordRepeat:
            print("Your passwords match, user confirmed")
            bol_UserPasswordMatch = True
        else:
            print("Incorrect input, please try again")
            Get_Password()

welcome()
