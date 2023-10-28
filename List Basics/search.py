num_of_string = int(input())
searched_word = input()
string_list = []
filtered_list = []
for string in range(num_of_string):
    string = input()
    string_list.append(string)
for i in string_list:
    if searched_word in i:
        filtered_list.append(i)
print(string_list)
print(filtered_list)

