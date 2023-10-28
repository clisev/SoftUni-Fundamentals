def remove_vowels(word):
    vowels = 'a', 'o', 'u', 'e', 'i'
    removed_vowels_word_list = [ch for ch in word if ch.lower() not in vowels]
    removed_vowels_word = "".join(str(c) for c in removed_vowels_word_list)
    return removed_vowels_word


text = input()
print(remove_vowels(text))
