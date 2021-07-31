# Syntax of function
# =========================

# def function_name(parameters):
#     """
#     document string (docstring)
#     """
#     statements

# function without argument

def welcome():
    """
    This function greets to the person
    """
    print("Hello Aziz Uddin. good morning ! ")

# Calling function
welcome()
print(welcome.__doc__)

# function with argument

def welcome(name):
    """
    This function greets to the person
    """
    print(f"Hello {name}. good morning ! ")

# Calling function
welcome('Mehedi Hasan')
welcome('Sayed Nashid')

# function without argument

def welcome(name, msg):
    """
    This function greets to the person
    """
    print(f"Hello {name}. {msg}! ")
welcome('Afrin Sultana','ki ranna hoyeche ?')
welcome('Sayed Nashid','Chole asho')

# Python arbitrary arguments
def welcome(*names):
    for n in names:
        print(f'Hello {n}')
welcome('Shahin','SID','Aziz','Naoushin','Tahmid','Mehedi')

def addition(*nums):
    for n in nums:
        print(n)
addition(5,3,4,7,8,9)

def addition(*nums):
    sum = 0
    for n in nums:
        sum = sum + n
    print(f'The sum is {sum}')
addition(5,3,4,7,8,9)

# Anonymous Function are also called Lambda Function
# syntax: functionName = lambda arguments : expression

show_Double = lambda x: x * 2
print(f'The double value is {show_Double(25)}')

def get_double(x):
    # print(x*2)
    return x * 2

get_double(2)
print(get_double(20))

myList = [100,1,5,4,6,8,11,3,12]
newList = list(filter(lambda x: (x % 2 == 0),myList))
print(newList)

# keyword arguments
def describe_Pet(petName, animaleType):
    print(f'\nI have a {animaleType}.')
    print(f'My {animaleType} \'s Name is {petName.title()}.')
describe_Pet(animaleType='Dog',petName='Tomy')

# Default values
def greet(name,msg='Good Morning'):
    print(f'Hello {name}, {msg}')
greet('Aziz Uddin')
greet("Tahmed","Good evening")

def buildProfile(first, last, **userInfo):
    proFile = {}
    proFile['first_Name '] = first
    proFile['last_Name '] = last
    for key, value in userInfo.items():
        proFile[key] = value

    return proFile
up = buildProfile('Afrin', 'Sultana', location = 'Dhaka', field = 'IT')
print(up)
