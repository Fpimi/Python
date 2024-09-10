
import random

num = random.randint(1, 5000)

r = int(input("Guess the number between 1-5000: "))

while r != num:
    if r < num:
        r = int(input(f"Wrong guess, try bigger that -> {r}:  "))
    else:
        r = int(input(f"Wrong guess, try less that -> {r}:  "))
print(f"You win¡¡¡¡ The number is: {num}")