###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Execution Control Structure, File Encoding, Using containers
# Description: Be able to use a file as input for your program, the program is
#              able to open and read the file and save data as a dictionary
#              while discarding useless data.
# Date: 03/08/2023
import os


def valid(str1):
    # this function validates that input is a valid input containing Upper
    # case letters, lower case letters and underscores.
    for i in str1:
        if not (i.isdigit() or i.isalpha() or i == '_'):
            return False
    return True


def main():
    # This is the container where I'll store the valid data from the file
    d = {}
    # This is the file to read, it will prompt the user for the correct file
    # until the user enters the correct file.

    filename = input("Enter the name of an input file:")
    while not os.path.exists(filename):
        print("Oops... An error occurred - Try again")
        filename = input("Enter the name of an input file:")

    # this line will open the file and read its contents
    with open(filename, 'r',  encoding='utf-8') as file:
        the_file = file
        line_num = 0
        for line in the_file:
            line = line.strip("\n")
            line_num += 1
            if valid(line):
                if line in d:
                    d[line].append(line_num)
                else:
                    d.update({line: [line_num, ]})
        for key in d:
            print(key, d[key])


if __name__ == '__main__':
    main()

'''
Enter the name of an input file:t2.dat
apple [1, 11]
1 [2, 3]
ball [4, 19]
art [5]
dog [6]
pen [8, 21]
rat [9]
4 [10]
carrot [13]
orange [15]
ant [16, 17, 18]
stick [20]
_ [22]
goodbye [25]

'''