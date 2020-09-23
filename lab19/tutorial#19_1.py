
import sys

ContactDetails = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange'
}

print("user input arguments: ", sys.argv[1:])

if not(len(sys.argv) > 2):
    print("Error! not enough input arguments. exiting")
    exit()

InputUserName = sys.argv[1]
InputUserPass = sys.argv[2]


try:
    if ContactDetails[InputUserName] == InputUserPass:
        print("Welcome Master")
    else:
        print("INTRUDER ALERT")
except KeyError:
    print("user name: ", InputUserName, ", is not in the data base!")

"""
Uri's comments:
==============

* Very good! This code works.
* You should not print the user's input (line 11). It's not necessary.
* In Python it's common to use variable names in lowercase. You can use "_" to separate between words.
  For example, use "input_user_name" instead of "InputUserName" and 
  "contact_details" instead of "ContactDetails".
* I think the assignment expected originally to use input and not the 
  command line arguments.
* You don't need empty lines at the beginning of Python files.
  
"""
