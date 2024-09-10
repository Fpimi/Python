

# Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

# The output should have the following format:

# Question:      [Question]
# Magic 8 Ball:  [Answer]

# Write code below 💖

import random

r = random.randint(1, 9)

a = "Yes - definitely."
b = "It is decidedly so."
c = "Without a doubt."
d = "Reply hazy, try again."
e = "Ask again later."
f = "Better not tell you now."
g = "My sources say no."
h = "Outlook not so good."
i = "Very doubtful."

input("Do your question: ")

if r == 1:
  print("Magic 8 ball:  " + a)
elif r == 2:
  print("Magic 8 ball:  " + b)
elif r == 3:
  print("Magic 8 ball:  " + c)
elif r == 4:
  print("Magic 8 ball:  " + d)
elif r == 5:
  print("Magic 8 ball:  " + e)
elif r == 6:
  print("Magic 8 ball:  " + f)
elif r == 7:
  print("Magic 8 ball:  " + g)
elif r == 8:
  print("Magic 8 ball:  " + h)
else:
  print("Magic 8 ball:  " + i)