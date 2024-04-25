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

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("O que você escolhe?\nDigite 0 para Pedra, 1 para Papel ou 2 para Tesoura."))
if user_choice >= 3 or user_choice < 0:
  print("Você escolheu o numero errado, você perdeu!")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0, 2)
  print(f"O computador escolheu {computer_choice}.")
  print(game_images[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("Você venceu!")
  elif computer_choice == 0 and user_choice == 2:
    print("Você perdeu!")
  elif computer_choice > user_choice:
    print("Você perdeu!")
  elif user_choice > computer_choice:
    print("Você venceu!")
  elif computer_choice == user_choice:
    print("Empate!")

