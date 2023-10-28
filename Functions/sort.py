def sort_numbers(nums):
    list_numbers = [int(num) for num in nums]
    sorted_list = sorted(list_numbers)
    return sorted_list


numbers = input().split()
print(sort_numbers(numbers))
