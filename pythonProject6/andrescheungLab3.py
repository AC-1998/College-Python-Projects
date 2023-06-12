###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Programming with Namespaces, Exception Control Flow, Data Analysis and
#         Handling input errors
# Description: Write a program that enforces the following expectations of a
#              data set file.
# Date: 03/14/2023
import os


def valid(int1):
    # This function validates that input is a valid input containing integers
    for i in int1:
        if not (i.isdigit()):
            return False
    return True


def _sum(arr):
    # This functions sums all items in an array
    i = 0
    for n in arr:
        i = i + n
    return i


def main():
    a = 0 # This counter will ensure that the program will execute 5 times
    b = [] # This array will store the contents of the file for later use
    while a < 5:
        # This lines will prompt the user for a filename
        filename = input("Please enter the file name: ")
        while not os.path.exists(filename):
            print("Invalid filename!")
            filename = input("Please enter the file name: ")

        a += 1
        line = 0
        with open(filename, 'r', encoding='utf-8') as file:
            for n in file:
                line += 0
                n = n.strip("\n")
                try:
                    b.append(int(n)) # Will append integers to the list
                except ValueError:
                    # In case there is not an integer in the list
                    print("Error: file contents invalid.")
            if valid(n) and len(b) == 11:
                try:
                    b.pop(0) # will remove the first line before the sum
                    ans = _sum(b)
                    print("The sum is:", ans)
                except TypeError:
                    print("Error: file contents invalid.")
            elif len(b) > 11:
                print("Error: End of file Expected")


if __name__ == '__main__':
    main()
'''
Please enter the file name: good.dat.html
The sum is: 55
Please enter the file name: bad1.dat.html
Error: End of file Expected
Please enter the file name: bad2.dat.html
Error: file contents invalid.
Error: End of file Expected
Please enter the file name: bad3.dat.html
Error: file contents invalid.
Error: End of file Expected
Please enter the file name: bad4.dat.html
Error: End of file Expected
'''