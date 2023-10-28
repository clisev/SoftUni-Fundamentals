money = input().split(", ")
int_money = [int(i) for i in money]

count_of_beggars = int(input())

sum_money = []
start_index = 0

while start_index < count_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(int_money), count_of_beggars):
        sum_for_current_beggar += int_money[current_index]
    sum_money.append(sum_for_current_beggar)
    start_index += 1

print(sum_money)



