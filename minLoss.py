# Minimum losses to endure from buying/selling goods at specified prices at consecutively dates.
def main():
    d = int(input())
    listsaleprice = []
    for i in range(0, d):
        listsaleprice.append(int(input()))

    minloss = None
    for i in range(0, d):
        for j in range(i+1, d):
            val = listsaleprice[i] - listsaleprice[j]
            if minloss is None and not val < 0:
                minloss = val
            if not minloss is None and minloss > val and not val < 0:
                minloss = val
    print(minloss)


main()
