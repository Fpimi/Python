



# guess = 0
# tries = 0

# while guess != 6 and tries < 5:
#   guess = int(input('Guess the number:  '))
#   tries = tries + 1

# if guess != 6:
#   print('You ran out of tries.')
# else:
#   print('You got it!')

# Write code below 💖

guess = 0
tries = 0
if tries == 3:
  print("You lost")

while guess != 6 and tries != 3:
  guess = int(input("Guess the number:  "))
  tries += 1
  #print(tries)
  if tries == 3:
    print("You lost")
  elif guess == 6:
    print("You got it!")