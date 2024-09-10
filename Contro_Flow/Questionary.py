


#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

#🦁 Gryffindor
#🦅 Ravenclaw
#🦡 Hufflepuff
#🐍 Slytherin
# Write code below 💖

Gryffindor = int(0)
Ravenclaw = int(0)
Hufflepuff = int(0)
Slytherin = int(0)

print("Q1) Do you like Dawn or Dusk?")
print("   1) Dawn")
print("   2) Dusk")

answer1 = int(input("answer: "))
ans1 = int(1)

if answer1 == 1:
  Gryffindor += ans1 and Ravenclaw + ans1
elif answer1 == 2:
  Hufflepuff += ans1 and Slytherin + ans1
else:
  print("Wrong input")

print("Q2) When I’m dead, I want people to remember me as:")
print("   1) The Good")
print("   2) The Great")
print("   3) The Wise")
print("   4) The Bold")

answer2 = int(input("answer: "))
ans2= int(2)

if answer2 == 1:
  Hufflepuff += ans2
elif answer2 == 2:
  Slytherin += ans2
elif answer2 == 3:
  Ravenclaw += ans2
elif answer2 == 4:
  Gryffindor += ans2
else:
  print("Wrong input")

print("Q3) Which kind of instrument most pleases your ear?")
print("   1) The violin")
print("   2) The trumpet")
print("   3) The piano")
print("   4) The drum")
answer3 = int(input("answer: "))
ans3 = int(4)

if answer3 == 1:
  Slytherin += ans3
elif answer3 == 2:
  Hufflepuff += ans3
elif answer3 == 3:
  Ravenclaw += ans3
elif answer3 == 4:
  Gryffindor += ans3
else:
  print("Wrong input")

print("Gryffindor has",Gryffindor, "points")
print("Ravenclaw has", Ravenclaw, "points")
print("Slytherin has", Slytherin, "points")
print("Hufflepuff has", Hufflepuff, "points")

if Gryffindor > Ravenclaw and Gryffindor > Slytherin and Gryffindor > Hufflepuff:
 print("Gryffindor is the winner with",Gryffindor, "points")

elif Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
 print("Ravenclaw is the winner with", Ravenclaw, "points")

elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
 print("Slytherin is the winner with", Slytherin, "points")

else:
  print("Hufflepuff is the winner with", Hufflepuff, "points")






