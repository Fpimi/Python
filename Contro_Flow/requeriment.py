


# Since 1927, "The Cyclone" rollercoaster has delighted riders visiting Coney Island in Brooklyn, New York. 🎢

# They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits)
# and need your help writing the program for it!)



height = float(input("What`s your height: "))
credits = float(input("How many credits have you got?: "))

if height >= 1.37 and credits >= 10:
  print("Enjoy the ride")

elif height < 1.37 and credits >= 10:
  print("You are not tall enough to ride")

elif height >= 1.37 and credits < 10:
  print("You don´t have enough credits")

else:
  print("You have not met either requeriment")