user_list = []

while True:

    x = input("Please Enter data: ")
    if not x:
        break
    else:
        user_list.append(x)

for element in user_list:
    print(element)
