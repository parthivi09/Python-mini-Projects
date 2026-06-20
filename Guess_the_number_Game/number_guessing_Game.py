# NUMBER GUESSING GAME
import random

def check_guess(user_guess,number):
    if(user_guess==number):
       return "correct"
    elif(user_guess>number):
        return "high"
    elif(user_guess<number):
        return "low"
       
    
number=random.randint(1,100)
attempts=7
print("------Welcome to Guess the Number!------")
print("You have only 7 Attempts!")

while True:
    user_guess=input("Enter a number to guess between 1 to 100 (q to quit) :")
    
    if(user_guess=='q'):
        print(f"Correct number is {number}")
        print("Thanks for playing.....")
        break
    user_guess=int(user_guess)
    if(user_guess>100 or user_guess<1):
        print("❌ Invalid input! Try again!")
        continue
    result=check_guess(user_guess,number)
    attempts-=1
    if (result=="correct"):
        print("🥳🎉Correct Guess!")
        print(f"you have done it in {7-attempts} Attempts!🥳🎉")
        break
    elif(result=="high"):
        print("📈Too High!Try a lower value!")
    elif(result=="low"):
        print("📉Too Low!Try a higher value!")
    print(f"You only have {attempts} attempts left!")
    
    if (attempts==0 and result!="correct"):
        print(f"\n🚫Game Over! You ran out of attempts!\nCorrect number:{number}")
        break
   

    
    
    
    
    
    
    
    
    
    