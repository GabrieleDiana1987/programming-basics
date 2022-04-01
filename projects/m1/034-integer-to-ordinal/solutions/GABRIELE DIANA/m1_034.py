# Convert an Integer to Its Ordinal Number

# Words like *first*, *second* and *third* are referred to as ordinal numbers. 
# In this exercise, you will write a function that takes an integer as its only parameter 
# and returns a string containing the appropriate English ordinal number as its only result. 
# Your function must handle the integers between 1 and 12 (inclusive). 
# It should return an empty string if the function is called with an argument outside of this range. 
# Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number. 
# Your main program should only run when your file has not been imported into another program.

# Documentation

# For this project solution you may use:

# - Functions

# Deadline

# This project requires to be completed in a maximum of **2 hours**


def trans_ordinal(number):
    map = {
        1 : "first",
        2 : "second",
        3 : "third",
        4 : "fourth",
        5 : "fifth",
        6 : "sixth",
        7 : "seventh",
        8 : "eight",
        9 : "ninth",
        10 : "tenth",
        11 : "eleventh",
        12 : "twelfth"
            }
    if number not in map:
        return " "
    else:
        return map.get(number)


def main():
    number = int(input("Please enter a number from 1 to 12: "))
    print(trans_ordinal(number))


if __name__ == '__main__':
    main()
