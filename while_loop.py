n = int(input())
count = 0
while count < n:
    print(count)
    count = count + 1


n = int(input())
m = n
count = 0
while count < n:
    print(m)
    m = m+1
    count = count + 1

#avg of n numbers
n = int(input())
sum = 0
count = 0
while count<n:
    count = count + 1
    sum = sum + count
avg = sum/n
print(avg)

#pattern
n = int(input())
count = 1
while count<=n:
    print("* " * count)
    count = count + 1

#print given string in line by line
a = input()
counter = 0
length_of_a = len(a)
while counter < (length_of_a):
    print(a[counter])
    counter = (counter + 1)

#pattern
n = int(input())
count = 1
while count<=n:
    print((str(count) + " ")* n)
    count = count + 1

#pattern
n = int(input())
count = 1
while count <= n:
    print((str(count) + " ") * count)
    count = count + 1