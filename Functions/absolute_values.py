def absolute_values():
    digits = input().split()
    int_digits = [float(digit) for digit in digits]
    abs_digit = []
    for digit in int_digits:
        digit = abs(digit)
        abs_digit.append(digit)
    print(abs_digit)


absolute_values()



