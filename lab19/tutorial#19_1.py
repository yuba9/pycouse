
import sys

ContactDetails = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange'
}

print("user input arguments: ", sys.argv[1:])

if not(len(sys.argv) > 2):
    print("Error! not enough input arguments, exiting")
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


