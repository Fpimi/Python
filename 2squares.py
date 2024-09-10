

# for i in range(5):
#  print('The square of ' + str(i) + ' is ' + str(i*i))

#The output would look like:

# The square of 0 is 0
# The square of 1 is 1
# The square of 2 is 4
# The square of 3 is 9
# The square of 4 is 16

# For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, nice to meet you!'
# you would like to replace the placeholder {name} with an actual name. This is string interpolation.

# The above program can be recreated using string interpolation using the {} sign:

# String interpolation

#  for i in range(5):
#   print(f'The square of {i} is {i*i}')
# Print all squares of 2:

print("All power of 2 are:  ")
for i in range(1, 12, ):
    print(f"- 2 square {i} - {2 ** i}")