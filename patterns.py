n = int(input()) #pyramid
for i in range(1,n+1):
    space = "  " * (n-i)
    star = "* " * (2*i -1)
    print(space + star)


n = int(input()) #inverted
for i in range(n+1):
    spaces = " " * i
    number = str(n) * n
    n = n - 1
    print(spaces + number)


n = int(input()) # M pattern
for i in range(1,n+1):
    star = "* " * i
    spaces = "  " * ((n * 2) - 2)
    n = n - 1
    print(star + spaces + star)

n = int(input())#
for i in range(1,n+1):
    number = (str(i) + " ") * i
    print(number)
n = n - 1
for i in range(0,n):
    number = (str(n) + " ") * n
    n = n - 1
    print(number)

n = int(input())#Butterfly
m = n
for i in range(1, n + 1):
    star = "* " * i
    spaces = "  " * ((n * 2) - 2)
    n = n - 1
    print(star + spaces + star)

for i in range(1, m):
    star = "* " * (m - i)
    spaces = "  " * (2 * i)
    print(star + spaces + star)



n = int(input())
for i in range(1,n+1):
    star = "* " * i
    spaces = " " * (n - i)
    between = " " * (n - i)
    print(spaces + star + between + spaces + star)