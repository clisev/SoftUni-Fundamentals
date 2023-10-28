number_of_electron = int(input())
lst = []
for num in range(1, number_of_electron):
    res = 2 * (num ** 2)
    if res > number_of_electron:
        res = number_of_electron
        lst.append(res)
        break
    lst.append(res)
    number_of_electron -= res
    if res > number_of_electron:
        if number_of_electron == 0:
            break
        res = number_of_electron
        lst.append(res)
        break
    if number_of_electron <= 0:
        break

print(lst)
