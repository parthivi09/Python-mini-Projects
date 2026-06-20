# ROCK-PAPER-SCISSOR GAME 
# rock=r=1
# paper=p=2
# scissor=s=3
import random

"""
This is done using computer-user choice see pattern in commented below
else:
    if (computer-user==-1 or computer-user==2 ):
        print("You win!")
    elif(computer-user==1 or computer-user==-2):
        print("You lose!")
    else :
        print("Something went wrong!")
"""

def check_win(computer,user):
    if(computer==user):
        return "draw"
    else:
        if(computer==1 and user==2):          #-1 
            return "win"
        elif(computer==1 and user==3):        #-2
            return "lose"
        elif(computer==2 and user==1):        #1
            return "lose"
        elif(computer==2 and user==3):        #-1
           return "win"
        elif(computer==3 and user==1):        #2
            return "win"
        elif(computer==3 and user==2):        #1
            return "lose"
        else:
            return "wrong"
        


user_score=0
computer_score=0

user_dict={"r":1,"p":2,"s":3}   
reverse_dict={1:"Rock",2:"Paper",3:"Scissors"}

print("~~~~~Welcome to Rock-Paper-Scissors!~~~~~")

while True:
    
    computer=random.choice([1,2,3])
    user_choice=input("Enter you choice ('r'for rock,'p' for paper,'s' for scissor,'q' to quit):")
    
    if(user_choice=='q'):
        print("FINAL SCORE")
        print(f"YOU:{user_score} | COMPUTER:{computer_score}")
        if(user_score>computer_score):
            print("You won the match!🎉")
        elif(user_score<computer_score):
            print("Computer won the match!😒")
        else:
            print("It is a tie!😶")
        print("Thanks for playing.....")
        break 
    
    if user_choice not in user_dict:
        print("Invalid choice!Try Again!")
        continue
  
    user=user_dict[user_choice]
    
    print(f"You entered:{reverse_dict[user]}\nComputer entered:{reverse_dict[computer]}")
    
    result=check_win(computer,user)
    
    if (result=="win"):
        print("You won this round!🎉")
        user_score+=1
    elif(result=="lose"):
        print("You lose this round!😢")
        computer_score+=1
    elif(result=="draw"):
        print("It is a draw")
    elif(result=="wrong"):
        print("Something went wrong!")
    
    
        



    
    
    
    
    
    
    
    
    
    
    
    
    