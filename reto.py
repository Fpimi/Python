
#   Two dices has been thrown, and you have to guess the total. You have 5 attempts. Good luke.

# Write code below 💖
import random

dc1 = random.randint(1, 6)
dc2 = random.randint(1, 6)

total = dc1 + dc2
i = 3
#print(total)
print("Two random dices has been thrown...")
num = int(input("What is total? (You have 5 attempts): "))
#print(i)
while num != total and i >= 0:
    #print(i)
    i -= 1
    if num < 2 or num > 12:
        num = int(input("Write number between 2-12: "))
    else:# num >= 2 or num <= 12:
        num = int(input("Wrong guess, Try again: : "))
if num == total and i != -1:
    print(f"You win¡¡¡¡ The total is: {total}")
elif num == total and i == -1:
    print(f"You win¡¡It was your last try¡¡ AMAZING¡¡¡ Total is: {total}")
else:
    print("You lose, You have no more attempts...")




