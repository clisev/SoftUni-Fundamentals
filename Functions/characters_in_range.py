def characters():
    first_char, second_char = input(), input()
    ascii_characters = []
    for current_char in range(ord(first_char) + 1, ord(second_char)):
        ascii_characters.append(chr(current_char))
    return " ".join(ascii_characters)


print(characters())
