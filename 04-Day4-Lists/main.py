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

rock_paper_array = [rock, paper, scissors]

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if choice not in ["0", "1", "2"]:
    print("Choose 0, 1, or 2")
    exit()

choice = int(choice)
pc_choice = random.randint(0, 2)

user_pick = rock_paper_array[choice]
pc_pick = rock_paper_array[pc_choice]

print(f"Your choice:\n{user_pick}")
print(f"Computer chose:\n{pc_pick}")

if choice == pc_choice:
    print("It's a draw!")
elif (choice == 0 and pc_choice == 2) or (choice == 1 and pc_choice == 0) or (choice == 2 and pc_choice == 1):
    print("You win!")
else:
    print("You lose!")
