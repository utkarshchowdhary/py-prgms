str = "Hello World"
res = ""

lis = str.split(" ")  # ["Hello", "World"]
size = len(lis)

"""
lis.reverse()  # ["World", "Hello"]
"""

for i in range(size):
    lis[i] = lis[i][::-1]

res = " ".join(lis)

print(res)
