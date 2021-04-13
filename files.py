fname = input("Enter file name: ")
try :
    fh = open(fname, 'r')
except : 
    print('Input file does not exist')
    quit()
    
for line in fh :
    line = line.rstrip().upper()
    print(line)
