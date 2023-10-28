num_of_numbers = int(input())
numbers_list = []
filtered_list = []
for num in range(num_of_numbers):
    current_num = int(input())
    numbers_list.append(current_num)

command = input()

if command == "even":
    for i in numbers_list:
        if i % 2 == 0:
            filtered_list.append(i)
elif command == "odd":
    for i in numbers_list:
        if i % 2 != 0:
            filtered_list.append(i)
elif command == "negative":
    for i in numbers_list:
        if i < 0:
            filtered_list.append(i)
elif command == "positive":
    for i in numbers_list:
        if i >= 0:
            filtered_list.append(i)
print(filtered_list)
