import random
from replit import clear

def number_guessing_game():

  global attempts
  attempts = int()

  def easy_mode():
    global attempts
    attempts += 10

  def hard_mode():
    global attempts
    attempts += 5

  def game():
    global attempts
    computer_pick = random.randint(1, 100)
    print(f'You have {attempts} remaining to guess the number.')
    user_number = int(input('Make a guess: '))
    attempts -= 1
    while attempts != 0:
      print(f'You have {attempts} remaining to guess the number.')
      if user_number > computer_pick:
        print('Too high.')
        attempts -= 1
      elif user_number < computer_pick:
        print('Too Low.')
        attempts -= 1
      else:
        break
      user_number = int(input('Guess again: '))
    if user_number == computer_pick:
      print(f'You got it, the awsner is {computer_pick}')
    else:
      print(f'You lose, the awsner is {computer_pick}')

    
  print("Welcome To The Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  
  x = 2
  while x > 1:
    difficulty = input("Choose a difficulty: type 'easy' or 'hard' ")
    if difficulty.lower() == 'easy':
      x -= 1
      easy_mode()
      game()
    elif difficulty.lower() == 'hard':
      x -= 1
      hard_mode()
      game()
    else:
      print("Invalid input. Try again!")
      
number_guessing_game()
play_again = False
while play_again == False:
  z = input("Would you like to play again? Y or N: ")
  if z.lower() == 'y':
    clear()
    number_guessing_game()
  elif z.lower() == 'n':
    play_again = True
    clear()
    print('thanks for playing')
  else:
    print('Invalid input. Try again!')