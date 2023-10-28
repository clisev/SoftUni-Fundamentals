def even_numbers(nums):
    list_numbers = [int(num) for num in numbers]
    list_even_numbers = [num for num in list_numbers if num % 2 == 0]
    return list_even_numbers


numbers = input().split()

print(even_numbers(numbers))
