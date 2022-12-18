#question1 a. finding the length of input string
name = "Python is a case sensitive language"
print(len(name))
# b. reverse the order of the string in one line code 
str2 = name[::-1]
print(str2)

# c. Using Slice function store “a case sensitive” in new string.

s1 = slice(10,35)
print(name[s1])


# d. Replace “a case sensitive” with “object oriented”
name2 = name.replace("a case sensitive","object oriented")
print(name2)

# e. Find index of substring “a” in the given input string.
print(name.find('a'))

# f. Remove the white spaces from the given input string.
str3 = name.replace(" ","")
print(str3)



