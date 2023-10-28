def smallest_number():
    first_num = int(input())
    second_num = int(input())
    third_num = int(input())
    numbers = [first_num, second_num, third_num]
    return min(numbers)


print(smallest_number())
