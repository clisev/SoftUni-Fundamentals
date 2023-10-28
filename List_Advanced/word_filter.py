text = input().split()
even_text = [word for word in text if len(word) % 2 == 0]
print("\n".join(even_text))
