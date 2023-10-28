def calculations():
    input_operator = input()
    first_num = int(input())
    second_num = int(input())
    if input_operator == "multiply":
        return first_num * second_num
    elif input_operator == "divide":
        return int(first_num / second_num)
    elif input_operator == "add":
        return first_num + second_num
    elif input_operator == "subtract":
        return first_num - second_num


print(calculations())
