#!/usr/bin/env python3

import os
from time import sleep
print('''
╔╗╔╗╔╗        ╔╗   ╔╗    ╔╗  ╔╗            ╔═══╗      ╔╗ ╔╗
║║║║║║        ║║   ║║    ║╚╗╔╝║            ║╔═╗║     ╔╝╚╗║║
║║║║║║╔══╗╔╗╔╗║║ ╔═╝║    ╚╗╚╝╔╝╔══╗╔╗╔╗    ║╚═╝║╔══╗ ╚╗╔╝║╚═╗╔══╗╔═╗
║╚╝╚╝║║╔╗║║║║║║║ ║╔╗║     ╚╗╔╝ ║╔╗║║║║║    ║╔╗╔╝╚ ╗║  ║║ ║╔╗║║╔╗║║╔╝
╚╗╔╗╔╝║╚╝║║╚╝║║╚╗║╚╝║      ║║  ║╚╝║║╚╝║    ║║║╚╗║╚╝╚╗ ║╚╗║║║║║║═╣║║
 ╚╝╚╝ ╚══╝╚══╝╚═╝╚══╝      ╚╝  ╚══╝╚══╝    ╚╝╚═╝╚═══╝ ╚═╝╚╝╚╝╚══╝╚╝
                                                                ''')
sleep(2)
def clear():
   os.system('clear')
clear()

TheQuestion = "Would you rather..."
Question1= {"A":"A: Be forced to wear wet socks for the rest of your life?",
            "B":"B: Or be allowed to wash your hair only once a year?"}

Question2= {"A":"A: Always have to tell the truth?",
            "B":"B: Or always have to lie?"}

Question3= {"A":"A: Only be able to whisper everything?",
            "B":"B: Or only be able to shout everything?"}

Question4= {"A":"A: Immerse yourself in a bathtub full of spiders?",
           "B":"B: Or a bathtub full of tobacco spit?"}

Question5= {"A":"A: Receive a lifetime supply of meals from your favorite restaurant?",
            "B":"B: Or receive a lifetime of free gasoline?"}

Questions= Question1, Question2, Question3, Question4, Question5

def game():
   #For loop to iterate over the questions
   for i in Questions:
      print(TheQuestion)
      sleep(1)
      print(i["A"])
      print(i["B"])
      sleep(0.5)
      input("Choose A or B?: ")
      clear()

def main():
    Again= True
    game()
    print("This is the end of the Questions! Come to play again next time!")

    while Again:
       user_input=input("Do you want to play again? yes or no: ").lower()
       if user_input == "yes":
          game()
       elif user_input == "no":
          print("Come play again next time!")
          Again= False
       else:
          print("that's not a valid response! Try again!")

main()
