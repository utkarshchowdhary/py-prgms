"""
a = 3
b = 34
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
 print("a is greater than b")
print("run always")

num = 12
if(num%2==0):
  print("Number is Even")
else:
  print("Number is odd")

print("h"+str(1))
que=input('who are you :')
print(type(que))

print(int(98.6))
print(float(1.2)*2,"hello","hf")

# infinite loop
while True :
  line = input("> ")
  if line == 'done' :
    break
  print(line)
print('Done')

#definite loop

for i in [5,4,3,2,1] :
  print(i)
print("Done")

#counted loop
friends = ['sal','mur','joe','que']
for i in range(len(friends)) :
  print('Happy New Year',friends[i])

print(type([]))
"""
"""
def computepay(h,r):
  if h<=40:
    return h*r
  if h>40:
    return 40*r + 1.5*r*(h-40)

hours= input("enter hours: ")
rate= input("enter rate per hours: ")
h=float(hours)
r=float(rate)
pay=computepay(h,r)
print("pay ", pay)

count=0
sum=0.0
while True :
  num= input("enter a number ")
  if num == "done": break
  try:
    fnum = float(num)
  except:
    print('invalid')
    continue
  count = count + 1
  sum = sum + fnum
 
print(count, sum, sum/count)
"""
"""
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try : 
        num = int(num)
    except :
        print('Invalid input')
        continue
    if largest is None and smallest is None :
        largest = num
        smallest = num
    elif largest < num :
        largest = num
    elif smallest > num :
        smallest = num
        
print("Maximum is", largest)
print("Minimum is", smallest)

#factorial of number
fact = 1
num = input('Enter a number ')
num = int(num)
while not num == 0 :
  fact = fact * num
  num = num - 1
print(fact) 

#Armstrong number
count = 0
res = 0
num = input('Enter a number ')
num = int(num)
temp = num
temp2 = num

while temp > 0 :
  temp=int(temp/10)
  print(temp)
  count = count+1

while temp2 > 0 :
  r = temp2%10
  res = res + r**count
  temp2=int(temp2/10)

print(num,res)
"""
"""
import math
r= input("enter radius ")
r= int(r)
area= math.pi*r**2
print(area)

#prime num
num = input('Enter a number ')
num = int(num)
i = 2
isprime=True

while not i==num :
  if num % i==0 :
    isprime=False
    break
  i=i+1
if isprime==True :
  print('is prime')
else :
  print('not prime')
"""
# fibonachi series
"""
num = input('Enter a number ')
num = int(num)
a = 0
b = 1
if num == 1 :
  print('0')
elif num == 2 :
  print('0')
  print('1')

else :
  print('0')
  print('1')
  while num>2 :
    c = a+b
    print(c)
    a=b
    b=c
    num=num-1
"""