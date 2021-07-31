sum = 1+2+3+4+5+6+7+8+9
print(sum)

a=15
b=5.5
c=True
d="Anik Islam"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a)
print(b)
print(c)
print(d)

studentName="Afrin Sultana"
studentAge=20

print(studentName,studentAge)
print("My name is " + studentName +" And I m "+ str(studentAge)+" years old ")
print("I am %s and I am %s years old " %(studentName, studentAge))
print("I am {0} and I am {1} years old ".format(studentName, studentAge))
print(f"I am {studentName} and I am {studentAge} years old")


x=input("Enter value for x: ")
y=input("Enter value for y: ")

# convert to integer - int(var)
# convert to float - float(var)
# result = int(x)+int(y)
result = float(x) + float(y)
print(f"addition is {result}")

result = float(x) - float(y)
print(f"subtraction is {result}")

result = float(x) * float(y)
print(f"multiplication is {result}")

try:

    result = float(x) / float(y)
    print(f"division is {result}")

    result = float(x) % float(y)
    print(f"modulus is {result}")


    result = float(x) ** float(y)
    print(f"exponent is {result}")
except:
    pass

print("=====================")
#  to generate compile error
# prin('&'*50) 
print('&'*50)

 