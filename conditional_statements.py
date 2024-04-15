#greatest among remainders
n = 12
rem1 = n%4
rem2 = n%5
if rem1>rem2:
    print(rem1)
else:
    print(rem2)


#last digit of a square
n = input() #15
num = int(n) #15
square = str(num ** 2) #225
length_square = len(square) - 1 #2
length = len(n) - 1 #1
last_digit = n[length] #5
last_digit_square = square[length_square] #5
if last_digit_square == last_digit:
    print("Equal")
else:
    print("Not an equal")


#armstring no using conditional statements
n = input() #4digit no
sum = (int(n[0]) ** 4) + (int(n[1]) ** 4) + (int(n[2]) ** 4) + (int(n[3]) ** 4)
if sum == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


#convert no of days to yr,weeks and days
n = int(input())
year = int(n/365)
rem = n%365
week = int(rem/7)
rem1 = rem % 7
days = rem1
print(year)
print(week)
print(days)

