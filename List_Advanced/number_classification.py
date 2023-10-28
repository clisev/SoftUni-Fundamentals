numbers = input().split(", ")
positive = [int(num) for num in numbers if int(num) >=  0]
negative = [int(num) for num in numbers if int(num) < 0]
even = [int(num) for num in numbers if int(num) % 2 == 0]
odd = [int(num) for num in numbers if int(num) % 2 != 0]

print(f'Positive: {", ".join(str(number) for number in positive)}')
print(f'Negative: {", ".join(str(number) for number in negative)}')
print(f'Even: {", ".join(str(number) for number in even)}')
print(f'Odd: {", ".join(str(number) for number in odd)}')
