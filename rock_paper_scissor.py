import random
item_list = ['rock','paper','scissors']
user_choice = input("Enter your move: rock, paper, scissor = ")
comp_choice=random.choice(item_list)
print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice==comp_choice :
    print("Both chooses Same: MATCH TIE")  
elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers Rock: COMPUTER WINS")
    if comp_choice == "scissors":
        print("Rock smashes Scissors: YOU WIN")
elif user_choice == "paper":
    if comp_choice == "rock":
        print("Paper covers Rock: YOU WIN" )
    else:
        print("Scissors cut Paper: COMPUTER WINS")
elif user_choice == "scissor":
    if comp_choice == "paper":
        print("Scissors cut Paper: YOU WIN")
    else:
        print("Rock smashes Paper: COMPUTER WIN")    

