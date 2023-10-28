first_line = input().split(", ")
second_line = input().split(", ")
new_list = []
for word in first_line:
    for second_word in second_line:
        if word in second_word:
            new_list.append(word)

new_list = list(dict.fromkeys(new_list))
print(new_list)

