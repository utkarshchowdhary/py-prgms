str = "hello world"

counts = dict()

for el in str:
    if el == 'a' or el == 'e' or el == 'i' or el == 'o' or el == 'u':
        counts[el] = counts.get(el, 0) + 1

print(counts)
