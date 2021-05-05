from random import randint

hn = randint(1, 100)
chancesLeft = 9
while chancesLeft > 0:
        en = int(input("Pls enter number to guess the hidden number : "))  # en stands for entered number
        if en == hn:
            print("\nCongratulations! You guessed the right number...its amazing yar...")
            print("You taken", (9 - chancesLeft), "chances to guess the number")
            exit(0)

        else:
            print("Oops! wrong number pls try again")

            if en > hn:
                print("Your number is high, enter low number")
            else:
                print("Your number is low, enter high number")

            chancesLeft-= 1
            print("Total chances left : ", chancesLeft)
            
print("You have no more chancesLeft....GAME OVER...")
