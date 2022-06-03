import random

print( "Winning Rules of the Rock Paper Scissors game as follows: \n"
+"Rock vs Paper->Paper wins \n"
+ "Rock vs Scissors->Rock wins \n"
+"Paper vs Scissors->Scissors wins \n")

while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = None
    player = input("What is your choice : R=Rock, P=Paper or S=Scissors? ")

    while player not in choices:  
        print("Not in choices. Try again!")
        player = input("What is your choice : R=Rock, P=Paper or S=Scissors? ")
      
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
        
    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")      
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")    
            
    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")      
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")   
            
    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")      
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")     
            
    play_again = input("Play again? (yes/no)" ).lower()    
    
    if play_again != "yes":
        break
print("Bye!")
    