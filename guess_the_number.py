import random

# Game Engine
def playGame(Nattempts):
    # Asking user to define game range
    print()
    Range=int(input("Do you wish to define range? if yes press 1 if no press any key and  the range will be 1-100: "))
    if Range==1:
        lower_bound=int(input("Enter lower bound: "))
        upper_bound=int(input("Enter upper bound: "))
    else:
        upper_bound=100
        lower_bound=0

    Tattempts=0
    # Generate a random number between 1 and 100
    guess_number=random.randint(lower_bound,upper_bound)

    print(guess_number,"for testing purpose")  #/// for testing purpose ///

    while Nattempts !=0:    #Keep running the loop until the number is guessed

        Tattempts+=1 #counting number of attempts
        
        Choosen_number=int(input("Guess Any Number In The Range{}{}-{}{}::".format("(",lower_bound,upper_bound,")")))
        if Choosen_number > guess_number :
            print("Oops! higher number")
            upper_bound=Choosen_number-1

        elif Choosen_number < guess_number :
            print("Oops! Lower number")
            lower_bound=Choosen_number+1
        
        elif Choosen_number == guess_number:
            print("Hurray! You've guessed the number the number in {}th attempt".format(Tattempts))
            break
        print()
        Nattempts -=1 #decreament statement
        print("{} attempt left".format(Nattempts))
        print()
    if Nattempts==0:    
       print()
       print("You don't have any attempt left, BETTER LUCK NEXT TIME!")


#Game Introduction
print("Welcome To The 'Number Guessing Game'::")
print()
print("""Enter Numbers Of Attempts You Want to play 
NOTE: NOT More Than 5""")
print()


# GAME LOOP
while True:
    # Asking for number of attempts
    while True:
      Nattempts=int(input("Enter Numbers Of Attempts:: "))
      if Nattempts <=5 and Nattempts > 0 :
            break     
      else: print("Enter The Number Of Attempts Again Please, PS: It should be range from 1-5")
    playGame(Nattempts)
    print()
    # Wanna Play Again
    playMore = int(input("Want to play More ? press 1 for play again and 0 for exit "))
    if playMore == 0:
        print("Thanks for playing!")
        break

