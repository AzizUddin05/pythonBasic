# example of dictionary
# ===========================
# dictionary is the collection of key value pairs

student = {1:'Ali',2:'Abdur Rahim',3:'Abdul Karim',4:'Tahmid',6:'SID'}
print(student)
print(student[4])
print(student[2])

employees = student.copy()
print(employees)
# modified or update data using key
employees.update({4:'Mehedi Hasan'})
print(employees)

employees.update({5:'Nashid'})
print(employees)

# delete data using del command
del employees[4]
print(employees)
print(dir(employees))
print('Display Items')
print('Emplyee Name %s'%(employees.items()))
print('Emplyee Name %s'%(list(employees.items())))

print('Display only keys')
for k in employees.keys() :
    print(k)

print('Display only values')
for k in employees.values() :
    print(k)

print('Key with value')
for k in employees.keys() :
    print(str(k)+"-"+str(employees[k]))

print('Total Item = '+str(len(employees)))

for k, v in employees.items() :
    # print(k,v)
    print(f'id: {k} name : {v}')

print(employees.get(3))
employees[9] = 'Kormokar'
print(employees)

emp = list(employees.keys())
print(emp)

emp.sort()
print(emp)

if 5 in employees :
    print('has found')
else :
    print('not found')

x = 1
while x<4:
    print(employees[x])
    x= x +1