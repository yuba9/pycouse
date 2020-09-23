import sys


def calc_average(lst):
    return sum(lst) / len(lst)

print("user input arguments ", sys.argv[1:])

if not(len(sys.argv) > 1):
    print("no input arguments entered")

new_list = []

try:
    for i in sys.argv[1:]:
        new_list.append(int(i))
except ValueError:
    print("Error! all input arguments must be numbers. exiting")
    exit()

list_average = calc_average(new_list)
print("average is: ", list_average)

print("listing the numbers which are greater then the average:")
for i in new_list:
    if i > list_average:
        print(i)

"""
Uri's comments:
==============

* Very good! This code works.
* Your program should handle no command line arguments or a number of grades
  different than 20.
* The assignment doesn't expect you to print the average. You should calculate it
  but not print it.
  
"""
