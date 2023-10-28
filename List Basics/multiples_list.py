factor = int(input())
count = int(input())

numbers_list = []

for num in range(1, count + 1):
    current_num = factor * num
    numbers_list.append(current_num)

print(numbers_list)
