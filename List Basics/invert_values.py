list_of_numbers = input().split()

opposite_numbers = []

for num in list_of_numbers:
    num = int(num)
    if num < 0:
        num = abs(num)
        opposite_numbers.append(num)
    else:
        num = -num
        opposite_numbers.append(num)

print(opposite_numbers)