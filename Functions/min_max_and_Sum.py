def find_min_max_numbers_and_sum(nums):
    list_numbers = [int(num) for num in nums]
    print(f"The minimum number is {min(list_numbers)}")
    print(f"The maximum number is {max(list_numbers)}")
    print(f"The sum number is: {sum(list_numbers)}")


numbers = input().split()
find_min_max_numbers_and_sum(numbers)
