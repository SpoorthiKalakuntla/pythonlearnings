#avg
n = int(input())
sum = 0
for i in range(1,n + 1):
    sum = sum + i
print(sum / n)

#pattern
n = int(input())
for i in range(1,n+1):
    print((str(i) + " ") * i)

#pattern
n = int(input())
for i in range(1,n+1):
    if i == n:
        print("+ " * n)
    else:
        print("* " * i)

#print n to 1
n = int(input())
for i in range(n):
    print(n)
    n = n - 1

#print the digit of a number
n = input()
d = ""
for i in n:
    d = d + i + " "
print(d)

#factorial
n = int(input())
product = 1
for i in range(1,n+1):
    product = product * i
print(product)

#print odd numbers from m to n
m = int(input())
n = int(input())
d = ""
for i in range(m,n+1):
    if i % 2 == 1:
        d = d + str(i) + " "
print(d)

#Armstrong number
n = input()
num = int(n)
length = len(n)
sum = 0
for i in n:
    power = int(i) ** length
    sum = sum + power
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#Factors of a given number
n = int(input())
d = ""
for i in range(1,n+1):
    if n % i == 0:
        d = d + str(i) + " "
print(d)

#Greatest among n numbers
n = int(input())
first_input = int(input())
greatest = first_input
for i in range(n - 1):
    number = int(input())
    if number > greatest:
        greatest = number
print(greatest)

#perfect number
n = int(input())
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#count of numbers from m to n that are divisible by 6
m = int(input())
n = int(input())
d = ""
sum = 0
for i in range(m,n+1):
    if i % 6 == 0:
        sum = sum + 1
        d = d + str(i) + " "
if sum == 0:
    print("No Numbers Found")
else:
    print(d)

#sum of n terms in power series
x = int(input())
n = int(input())
m = 2
sum = 0
for i in range(1,n+1):
    if i % 2 == 1:
        power = x ** m
        m = m + 2
        sum = sum + power
    if i % 2 == 0:
        power = -(x) ** m
        m = m + 2
        sum = sum + power
print(sum)


#reverse of string
word = "input"
d = ""
for i in word:
    d = i + d
print(d)

#sum of k powers
n = int(input())
k = int(input())
sum = 0
for i in range(1,n+1):
    power = i ** k
    sum = sum + power
print(sum)