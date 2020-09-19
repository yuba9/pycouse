

file_handler = open('words.txt', "r")
general_lines = file_handler.readlines()
file_handler.close()

# the core algorithm is to build a-b-c histogram of each word's letters and then compare them
def is_anagram(str1, str2):
    abc_historgram1 = {}
    abc_historgram2 = {}

    if len(str1) != len(str2):
        return False

    for letter in str1:
        if letter in abc_historgram1:
            abc_historgram1[letter] = abc_historgram1[letter]+1
        else:
            abc_historgram1[letter] = int(1)

    for letter in str2:
        if letter in abc_historgram2:
            abc_historgram2[letter] = abc_historgram2[letter]+1
        else:
            abc_historgram2[letter] = int(1)

    is_identical_flag = 1
    for char_num in range(97, 110):
        char = chr(char_num)
        if char in abc_historgram1:
            if char in abc_historgram2:
                if abc_historgram1[char] != abc_historgram2[char]:
                 is_identical_flag = 0
            else:
                is_identical_flag = 0

    if is_identical_flag == 1:
        return True
    else:
        return False




final_list = []
while True:
    if len(general_lines) == 0:
        break

    temp_list = []
    idx = 1
    while True:

        if idx >= len(general_lines):
            temp_list.append(general_lines[0].rstrip())
            general_lines.pop(0)
            break;
        if is_anagram(general_lines[0].rstrip(), general_lines[idx].rstrip()):
            temp_list.append(general_lines[idx].rstrip())
            general_lines.pop(idx)
            continue
        else:
            idx = idx +1
    final_list.append(temp_list)   #adding entry (not concatanating)

for i in final_list:
    for j in i:
        print(j," ",end ="")
    print("")