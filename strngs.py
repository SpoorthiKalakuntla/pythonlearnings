#string concatenation and string repetition
s = "python"
s = ("* " * 3) + s + (" *" * 3)
print(s)

#length of the string
username = "spoorthi"
length = len(username)
print(length)


#accessing character in string and slicing
word = "nani"
print(word[0])
print(word[:4])

#last character of a given word
word = "January"
length = len(word) - 1
print(word[length])

print(length/2)

#input from user
name = input()
print(name)

#check data type and converisons
a = "20"
b = int(a)
c = float(a)
print(c)
print(type(a))
print(type(b))
print(type(c))