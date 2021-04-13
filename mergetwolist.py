listone = []  # 1, 2, 3, 4, 5
listtwo = []  # 6, 7, 8
reslist = []

sizeone = int(input("Enter size one: "))
sizetwo = int(input("Enter size two: "))

print("Enter values for list one:")
for i in range(sizeone):
    listone.append(int(input()))

print("Enter values for list two:")
for i in range(sizetwo):
    listtwo.append(int(input()))

size = sizeone if sizeone > sizetwo else sizetwo

for i in range(size):
    if i < sizeone:
        reslist.append(listone[i])
    if i < sizetwo:
        reslist.append(listtwo[i])

print(reslist)
