


## Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

## First, create a ph variable and ask the user for a value between 0 and 14.

## Write an if, elif, else statement that:

## If ph is greater than 7, output "Basic".
## If ph is less than 7, output "Acidic".
## Else, output "Neutral".

# Write code below 💖
try:
  ph = float(input("What is pH level (0-14)?: "))
  print("The liquid is:")

  if 7 < ph <= 14:
    print("Basic")

  elif 0 <= ph < 7:
    print("Acidic")

  elif ph > 14:
    print("This is invalid level")

  elif ph < 0:
    print("This is invalid level")

  elif ph == 7:
    print("Neutral")

  elif ph(str):
    print("This is invalid charapter")

  else:
    print("This is invalid level")

except ValueError:
  print("You must write a number between 0-14")
