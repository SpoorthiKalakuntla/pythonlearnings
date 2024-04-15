a = int(input())
b = int(input())
print(a > b)
print(a < b)
print(a != b)
print(a == b)
print(a <= b)
print(a >= b)

#check part of a string
a = input()    #repeat
b = input()     #pea
i = int(input())    #2
length_b = len(b)
part = i + length_b
print(a[i:part] == b)

#exponent operator
a = 2
b = 3
print(a ** b)