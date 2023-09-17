import random
from builtins import print, input
user_score = 0
computer_score=0
def get_user_choice():
    while True:
        user_choice=input("choose rock, paper, or scissors:").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. please choose rock , paper, or scissors.")
def get_computer_choice():
     return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
     if user_choice==computer_choice:
         return "It's a tie!"
     elif(
        (user_choice=='rock' and computer_choice=='scissors') or
        (user_choice=='paper' and computer_choice=='rock') or
        (user_choice=='scissors' and computer_choice=='paper')
     ):
         return "You Win!"
     else:
         return "Computer wins!"
def play_game():
     global user_score, computer_score
     user_choice= get_user_choice()
     computer_choice= get_computer_choice()
     print(f"your choice: {user_choice}")
     print(f"computer's choice:{computer_choice}")

     result=determine_winner(user_choice, computer_choice)
     print(result)

     if result=="You Win!":
         user_score += 1
     elif result=="Computer wins!":
         computer_score += 1
     print(f"Score - you:{user_score},Computer:{computer_score}")
while True:
     play_game()
     play_again=input("Do you want to play again?(yes/no):").lower()
     if play_again!='yes':
         break
print("Thanks for playing!")