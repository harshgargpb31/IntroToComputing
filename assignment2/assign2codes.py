#Assignment 2
print("Prog.1")
str1 = "Python is a case sensitive language"
print(len(str1))

# b. Reverse the order of the string in one line code.
str1 = "Python is a case sensitive language"
print(str1[::-1])

# c. Using Slice function store “a case sensitive” in new string.
str1 = "Python is a case sensitive language"
str2 = str1[10:26]
print(str2)

# d. Replace “a case sensitive” with “object oriented”.
str1 = "Python is a case sensitive language"
print(str1.replace("a case sensitive", "object oriented"))

# e. Find index of substring “a” in the given input string.
str1 = "Python is a case sensitive language"
print(str1.find("a"))

# f. Remove the white spaces from the given input string.
str1 = "Python is a case sensitive language"
#to replace white spaces we can replace spaces with blank
print(str1.replace(" ", ""))

print("Prog.2")

#input name,sid,course and cgpa from the user
inp_name = input("Hi Pecian, Please enter your name\n")
inp_SID = input("Please enter you SID[eg.2110XXXX]\n")
inp_course = input("Please enter your department[eg.CSE,ECE,ELE,etc.]\n")
inp_CGPA = input("Please enter your CGPA[eg.5.5,9.0,10.0]\n")

print("Hey,",inp_name, "Here!")
print("My SID is", inp_SID)
print("I am from", inp_course, "department and my CGPA is", inp_CGPA)

print("Prog.3")
a=56
b=10
#3a
print(a&b)
#3b
print(a|b)
#3c
print(a^b)
#3d left shift both by 2
print(a<<2)
print(b<<2)
#3e right shift a by 2 and b by 4
print(a>>2)
print(b>>4)

print("Prog.4")


#firstly take the input string
inp_str = input("Enter your string\n")
#now find the string using 'in' function
if "name" in inp_str:
#print yes or no
    print("Yes")
else:
    print("NO")

print("Prog.5")
#firstly input three numbers
a = int(input("Enter first length\n"))
b = int(input("Enter second length\n"))
c = int(input("Enter third length\n"))
#now check one by one that any of the three lengths is greater than the sum of the other two or not
if a+b<=c or a+c<=b or c+b<=a:
    print("No")
else:
    print("Yes")

print("Prog.6")
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
num=a^b
Count_flipped_bit=0
while(num!=0):
    num=num&(num-1)
    Count_flipped_bit+=1
print("Number of bits needed to be flipped to convert a to b is:",Count_flipped_bit)