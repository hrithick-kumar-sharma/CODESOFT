import random
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

game_image = [rock,paper,scissors]

user_choice= int(input("what is choice type 0 for rock and type 1 paper and 2 scissors"))
if user_choice >=0 and user_choice<=2:
    print(game_image[user_choice])
computer_choice = random.randint(0 ,2)
print("computer chose")
print(game_image[computer_choice])
if user_choice>=3 and user_choice<0:
    print("invalid number")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
else:
        print("You lose!")

