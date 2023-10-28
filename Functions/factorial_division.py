from math import factorial


def divide_factorials_numbers(first_num, second_num):
    factorial_first_number = factorial(first_number)
    factorial_second_number = factorial(second_number)
    result = factorial_first_number / factorial_second_number
    formated_resultat = f"{result:.2f}"
    return formated_resultat


first_number, second_number = int(input()), int(input())
print(divide_factorials_numbers(first_number, second_number))
