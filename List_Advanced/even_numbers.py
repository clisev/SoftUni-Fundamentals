numbers = list(map(int, input().split(", ")))
is_index_found = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
even_indices = list(filter(lambda a: a != "no", is_index_found))
print(even_indices)
