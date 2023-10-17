import random
def randomselect(inputstring) :

    testlist2 = ['rock', 'paper', 'scissor']
    testlist = [x.upper() for x in testlist2]
    selectval = random.choice ( testlist )
    print ( "Computer selected :" + selectval )
    if inputstring.upper() in testlist:
        if selectval == inputstring.upper():
            print(f"Both players selected {inputstring}. It's a tie!")
        elif inputstring.upper() == "ROCK":
            if selectval == "SCISSORS": print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif inputstring == "PAPER":
            if selectval == "ROCK":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif inputstring == "SCISSOR":
                if selectval == "PAPER":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! You lose.")
    else:
        print("Invalid Entry")

if __name__ == '__main__' :
    inputstring = str ( input ( "Please enter your Selection" ) )
    print ( "You selected :" + inputstring )
    randomselect ( inputstring )

