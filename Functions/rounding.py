def rounding():
    given_numbers = input().split()
    int_given_nums = [float(num) for num in given_numbers]
    round_numbers = [round(n) for n in int_given_nums]
    return round_numbers


print(rounding())