hn = 16 # hn stands for hidden number 
chancesLeft = 9
chancesTaken = 0
while (True):
    if chancesLeft == 0 or chancesTaken == 9:
         print("You have no more chancesLeft....GAME OVER...")
         break
    else:
        en = int(input("Pls enter number to guess the hidden number : "))  # en stands for entered number
        chancesTaken = chancesTaken + 1
        if en == hn:
            print("\nCongratulations! You guessed the right number...its amazing yar...")
            print("\nYou taken",chancesTaken, "chances to guess the number")
            break
        else:
            print("\nOops! wrong number pls try again")
            if en > hn:
                print("Your number is high, enter low number")
            else:
                print("Your number is low, enter high number")
            chancesLeft = chancesLeft - 1
            print("Total chancesLeft left : ", chancesLeft)
            
            c = sum((3,5))
            