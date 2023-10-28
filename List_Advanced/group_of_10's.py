numbers = list(map(int, input().split(", ")))
current_group_of_numbers = 10

while numbers:
    filtered_list_for_current_group = []
    for current_num in numbers:
        if current_num <= current_group_of_numbers:
            filtered_list_for_current_group.append(current_num)
    print(f"Group of {current_group_of_numbers}'s: {filtered_list_for_current_group}")
    current_group_of_numbers += 10
    numbers = [num for num in numbers if num not in filtered_list_for_current_group]
