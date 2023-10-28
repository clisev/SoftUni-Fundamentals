def is_palindrome_number(nums):
    if nums == nums[::-1]:
        return True
    return False


numbers = input().split(", ")
for number in numbers:
    print(is_palindrome_number(number))
