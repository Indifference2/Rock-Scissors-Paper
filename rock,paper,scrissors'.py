rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


list_choices = ["rock","scissors","paper"]
choice_machine = random.choice(list_choices)

    
user_choice = int (input ("'0' for rock, '1'for scissors, '2' for paper------->"))
    
       
if (choice_machine == "rock" and list_choices[user_choice] == "scissors"):
       
        print ("\n")
        print("You pick",scissors)
        print ("The machine pick",rock)
        print ("You lose")
elif (choice_machine == "rock" and list_choices[user_choice] == "paper"):
        print ("\n")
        print("You pick",paper)
        print ("The machine pick",rock)
        print ("You win")
elif (choice_machine == "rock" and list_choices[user_choice] == "rock"):
        print ("\n")
        print("You pick",rock)
        print ("The machine pick",rock)
        print ("It is a tie")
  
if (choice_machine == "scissors" and list_choices[user_choice] == "rock"):
        print ("\n")
        print("You pick",rock)
        print ("The machine pick",scissors)
        print ("You win")
elif (choice_machine == "scissors" and list_choices[user_choice] == "paper"):
        print ("\n")
        print("You pick",paper)
        print ("The machine pick",rock)
        print ("You lose")
elif (choice_machine == "scissors" and list_choices[user_choice] == "scissors"):
        print ("\n")
        print("You pick",scissors)
        print ("The machine pick",scissors)
        print ("It is a tie")  
    
if (choice_machine == "paper" and list_choices[user_choice] == "rock"):
        print ("\n")
        print("You pick",rock)
        print ("The machine pick",paper)
        print ("You lose")
elif (choice_machine == "paper" and list_choices[user_choice] == "scissors"):
        print ("\n")
        print("You pick",scissors)
        print ("The machine pick",paper)
        print ("You win")
elif (choice_machine == "paper" and list_choices[user_choice] == "paper"):
        print ("\n")
        print("You pick",paper)
        print ("The machine pick",paper)
        print ("It is a tie")