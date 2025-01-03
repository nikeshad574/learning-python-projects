import random

options = ["rock", "paper", "scissor"]

playerWin = 0
computerWin = 0
tie = 0

while True:
    userInp = input("\nChoose 0=rock, 1=paper, 2=scissor, q=quit: ")
    computerGuess = random.choice(options)

    if userInp == "q": 
        print("Thankyou for playing!")
        break

    if userInp.isdigit():
        userInp = int(userInp)
    else:
        print("Invalid Input")
        continue

    if userInp not in [0, 1, 2]:
        print("Invalid!")
        continue
    elif options[userInp] == computerGuess:
        print(f"Both Played {computerGuess}")
        print("Tie!")
        tie += 1
    else:
        print(f"User: {options[userInp]}")
        print(f"Computer: {computerGuess}")

        if options[userInp] == "scissor" and computerGuess == "paper":
            print("You Win!")
            playerWin += 1
        elif options[userInp] == "paper" and computerGuess == "rock":
            print("You Win!")
            playerWin += 1
        elif options[userInp] == "rock" and computerGuess == "scissor":
            print("You Win!")
            playerWin += 1
        else:
            print("You Loose!")
            computerWin += 1
        
    print(f"User Score = {playerWin} , Computer Score = {computerWin}, Tie = {tie}")