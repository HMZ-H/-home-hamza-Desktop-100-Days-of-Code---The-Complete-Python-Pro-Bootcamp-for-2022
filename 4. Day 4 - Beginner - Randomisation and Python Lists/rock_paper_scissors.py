import RPS_ASCII_Art
import random 

game_images = [RPS_ASCII_Art.rock, RPS_ASCII_Art.paper, RPS_ASCII_Art.scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:   
    print("User chose")
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose ")
    print(game_images[computer_choice])

    if computer_choice ==0 and user_choice == 2:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose")

    elif computer_choice == user_choice:
        print("It's a draw")

