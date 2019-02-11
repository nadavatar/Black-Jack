from random import randint

userScore = 0
computerScore = 0
isUserPlaying = True
isComputerPlaying = True
isUserLost = False
isComputerLost = False

userScore += randint(1, 13)
print("Your score is: " + str(userScore))

choice = raw_input("If you want another card enter y, otherwise enter n:\n")
if choice == "n":
    isUserPlaying = False

while(userScore < 22 and isUserPlaying):

    userScore += randint(1, 13)
    if userScore > 21:
        print("You have: " + str(userScore) + " You Lost!")
        isUserPlaying = False
        isUserLost = True

    else:
        print("Your score is: " + str(userScore))
        choice = raw_input("If you want another card enter y, otherwise enter n:\n")
        if choice == "n":
            isUserPlaying = False

if isUserLost != True:

    computerScore += randint(1, 13)
    if computerScore > userScore:
        print("The computer score is: " + str(computerScore))
        print("You have lost...")
        isUserLost = True
    
    while(isComputerPlaying and computerScore < 21 and computerScore < userScore):

        computerScore += randint(1, 13)
        
        if computerScore < 21 and computerScore < userScore:
            print("The computer score is: " + str(computerScore))

        elif computerScore < 21 and computerScore > userScore:
            print("The computer score is " + str(computerScore))
            print("The computer won!")
            isComputerPlaying = False

        else:
            print("The computer score is " + str(computerScore))
            print("You Have Won!")
            isComputerPlaying = False
            isComputerLost = True