###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: User Input, Arithmetic, Data Types, Importing modules
# Description: this code is an application that will take the sum of the numbers
#              in a Student GID and the number of letters in your last name and
#              perform arithmetic operations
# Date: 02/07/2023


from datetime import datetime

num_let = input("What is your family name: ")
my_id = input("Enter your Student ID: ")

numLength = len(num_let)
# this line uses maps and list to convert a string number to a list of integers
my_id = list(map(int, str(my_id)))
my_id = sum(my_id)

# Here is where all the arithmetic operations are calculated
expression1 = my_id / 2
expression2 = my_id % 2
expression3 = sum(range(2, numLength))
expression4 = my_id + numLength
expression5 = abs(numLength - my_id)
expression6 = my_id / (numLength + 1100)
expression7 = (numLength % numLength) and (my_id * my_id)
expression8 = 1 or (my_id / 0)
expression9 = round(3.15, 1)

# Here I'll print the results of the operations
print("my_id is: ", my_id)
print("n_let is: ", numLength)
print("expression1: %.2f" % expression1)
print("expression2: ", expression2)
print("expression3: ", expression3)
print("expression4: ", expression4)
print("expression5: ", expression5)
print("expression6: %.2f" % expression6)
print("expression7: ", expression7)
print("expression8: ", expression8)
print("expression9, %.2f" % expression9)
print(datetime.now())




