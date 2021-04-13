name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

lst = list()
for k,v in counts.items() :
    newtup = (v,k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

#lst = sorted([(v,k) for k,v in counts.items()],reverse=True)

for v,k in lst[:10] :
    print(k,v)