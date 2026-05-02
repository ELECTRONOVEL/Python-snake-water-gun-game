
     # my first project mistakes can happen !!


'''

Snake = 1

water = -1

gun = 0

'''

import random


options = {"snake":1,"water":-1,"gun":0}

reverse = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([1,-1,0])



user_choice = str(input("Enter Your Choice(snake/water/gun) :  ")).strip().lower()


if user_choice not in options:
    print("Enter a Valid Input(snake/water/gun)")

    exit()

user_int = options[user_choice]
if user_choice in options:
    def Result():
        if computer == user_int:
          return "Its a Draw !"
    
        elif user_int == 1 and computer==-1:
          return "You WIN !"
    
        elif user_int==1 and computer==0:
          return "You LOSE HAHA !"
    
        elif user_int == 0 and computer== 1:
          return "You WIN !"
    
        elif user_int==0 and computer == -1 :
          return "You LOSE \nSkill Issue ?"
    
        elif user_int==-1 and computer == 0:
          return "You WIN, Lucky Comrade!"
    
        elif user_int== -1 and computer == 1:
           return "You Lose !, Try Harder"
    
        else:
          return "Something Went Wrong ! ,\nEnter One option from Snake,Water or Gun"
        


    

print(f" Computer choosen option : {reverse[computer]}")

print(Result())

    




    
    