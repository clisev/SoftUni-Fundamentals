employees_happiness = list(map(int, input().split()))
factor = int(input())
multiply_happiness = []

for i in employees_happiness:
    res = i * factor
    multiply_happiness.append(res)

average = sum(multiply_happiness) / len(multiply_happiness)

happy_employees = [i for i in multiply_happiness if i >= average]

if len(happy_employees) >= len(employees_happiness)/2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
