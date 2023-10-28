def odd_even_sum():
    number = int(input())
    str_number = str(number)
    numbers_list = []
    for i in str_number:
        numbers_list.append(int(i))

    even_numbers = [num for num in numbers_list if num % 2 == 0]
    odd_numbers = [num for num in numbers_list if num % 2 != 0]
    return f"Odd sum = {sum(odd_numbers)}, Even sum = {sum(even_numbers)}"


print(odd_even_sum())
