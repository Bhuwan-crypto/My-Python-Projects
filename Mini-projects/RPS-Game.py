"""
Workflow of project:
1-Input from user(rock,paper,scissor)
2-computer choice (random)
3-Result

HOW:
a-Rock
rock - rock =tie
rock - paper = paper win
rock - scissor =rock win

b-paper
paper-paper = tie
paper - rock = paper win
paper - scissor = scissor win

c- scissor
scissor - scissor = tie
scissor - paper = scissor win
scissor - rock = rock win
"""
import random
item_list = ["Rock","Paper","Scissor"] #list data type

user_choice = input ("Enter your move = Rock,Paper,Scissor =")
comp_choice = random.choice(item_list)#chooses random item from list

print(f"user choice ={user_choice} , computer choice ={comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print ("Rock smashes scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper = Computer win")
    else:
        print("Paper covers Rock = You win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper = You win")
    else:
        print("Rock smashes scissor = Computer win")