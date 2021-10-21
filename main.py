# Rock Paper Scissors Game V2
# Created By Alex Tomsovic
# Enjoy!

import elements
import random            
import click          
def clrscr():

    click.clear()
print(elements.welcome_elem)       
play = "Y"
while play == "Y" or play == "y": 
  choice = int(input("Enter Your Choice:\nType 0 for Rock , 1 for Paper , 2 for scissors:\n)> "))
  if choice == 0 or choice == 1 or choice == 2:
    print("Your choice:")
    if choice == 0:
      print(elements.rock_elem)
    elif choice == 1:
      print(elements.paper_elem)
    elif choice == 2:
      print(elements.scissors_elem)
    else:
      print("Enter a number: 0 , 1 , 2 ")  
    print("Computer's choice :")
    choice_computer = random.randint(0,2)  

    if choice_computer == 0:
      print(elements.rock_elem)
    elif choice_computer == 1:
      print(elements.paper_elem)
    elif choice_computer == 2:
      print(elements.scissors_elem)
    string_choice = str(choice)
    string_choice_computer = str(choice_computer)
    num = string_choice+string_choice_computer
    if num == "02"or num == "10" or num == "21":       

      print("You Won :) , Good Job!")
    elif num == "00" or num == "11" or num == "22":
        print("It's a Tie :| , You're a Tough Opponent")
    else:
      print("You lost. Better luck next time! ")
  else:
    print("Please Enter a valid number 0 , 1 , 2 .")
  print("\r")
  play = input("Do you want to play again?\nIf Yes then type : 'Y' , if u want to exit type 'N':\n)> ")
  clrscr()                                                            
print("\r")
print("Thanks For Playing , Come Back Soon :)")
