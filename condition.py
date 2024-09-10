
# Run program.
# It will generate 2 randoms numbers between 1-100.
# If both numbers are less or equal than 20, you win. Else you must keep trying.

# Write code below 💖
import random

a = random.randint(1, 100)
b = random.randint(1, 100)

#print(a, b)

if a <= 20 and b <= 20:
  c = True
else:
  c = False

print("If A, that is:  ")
print(a)
#print(" ")
print("If B , that is:  ")
print(b)
#print(" ")
print("Both are less or equal than 20, C is True. Else C is False")
print("C is:  ")
#print(" ")
print(c)
#print(" ")
if not c:
  print("Keep trying")
else:
  print("!!!!!CONGRATULATIONS!!!!")

