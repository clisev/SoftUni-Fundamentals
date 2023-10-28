def check_password(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid


entered_password = input()
password_is_valid = check_password(entered_password)
if password_is_valid:
    print("Password is valid")