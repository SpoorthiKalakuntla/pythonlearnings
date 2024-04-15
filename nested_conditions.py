#electricity bill
units = int(input())
if units < 50: #charge 2 per unit for (0 to 50)
    bill = 2 * units
elif units < 150: #charge 3 per unit for (51 to 150)
    bill = (2 * 50) + (3 * (units - 50))
elif units < 250: #charge 5 per unit for (151 to 250)
    bill = (2 * 50) + (3 * 100) + (5 * (units - 150))
else:
    bill = (2 * 50) + (3 * 100) + (5 * 100) + (8 * (units - 250))
charge = (20/100) * bill
total_bill = bill + charge
print(total_bill)

#smallest among 3 numbers
a = int(input())
b = int(input())
c = int(input())
if a<b and a<c:
    print(a)
elif b<c:
    print(b)
else:
    print(c)

#check the given value is leap yr or not
year = int(input())
if (year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print(str(year) + " is a leap year")
        else:
            print(str(year) + " is not a leap year")
    else:
        print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")


#last char of string contains "T/H/K" then print the value
s = input()
length = len(s) - 1
last_char = s[length]
char = int(s[0:length])
if last_char == "T":
    print(char * 10)
elif last_char == "H":
    print(char * 100)
elif last_char == "K":
    print(char * 1000)

#prints minimun no of 2000,500,200,50,20,5,2,1 rupee notes
a = int(input())
two_thousand = int(a / 2000)
rem = a % 2000
five_hundred = int(rem / 500)
rem1 = rem % 500
two_hundred = int(rem1 / 200)
rem2 = rem1 % 200
fifty_ruppee = int(rem2 / 50)
rem3 = rem2 % 50
twenty_ruppee = int(rem3 / 20)
rem4 = rem3 % 20
five_ruppee = int(rem4 / 5)
rem5 = rem4 % 5
two_ruppee = int(rem5 / 2)
rem6 = rem5 % 2
one_ruppee = int(rem6 / 1)
print("2000:" + str(two_thousand) + " 500:" + str(five_hundred) + " 200:" + str(two_hundred) + " 50:" + str(fifty_ruppee) + " 20:" + str(twenty_ruppee) + " 5:" + str(five_ruppee) + " 2:" + str(two_ruppee) + " 1:" + str(one_ruppee))


#day name
d = input()
n = int(input())
if d == "Sunday":
    day = 0
elif d == "Monday":
    day = 1
elif d == "Tuesday":
    day = 2
elif d == "Wednesday":
    day = 3
elif d == "Thursday":
    day = 4
elif d == "Friday":
    day = 5
elif d == "Saturday":
    day = 6
target_day = day + (n - 1)
target_day = target_day % 7
if target_day == 0:
    print("Sunday")
elif target_day == 1:
    print("Monday")
elif target_day == 2:
    print("Tuesday")
elif target_day == 3:
    print("Wednesday")
elif target_day == 4:
    print("Thursday")
elif target_day == 5:
    print("Friday")
elif target_day == 6:
    print("Saturday")