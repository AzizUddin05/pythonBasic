"""
x = [3,6,2,9]

x = [6]
x = 1
x = 9
print(x)
"""
motorCycles = ['Honda','Yamaha','Sujuki']
print(motorCycles)

print(motorCycles[0])
print(motorCycles[1])
print(motorCycles[2])

# change data
motorCycles[1] = 'ducti'
print(motorCycles)

# append
fruits = []
fruits.append('Mango')
fruits.append('Bnana')
fruits.append('Orange')

fruits.insert(1,'Apple')
fruits.insert(3,'Grape')

print(fruits)

# remove
del fruits[3]
print(fruits)
fruits.pop() # last in first out LIFO
print(fruits)
fruits.remove('Apple')
print(fruits)

fruits.remove('Mango')
print(fruits)

fruits.remove('Bnana')
print(fruits)

cars = ['bmw', 'audi', 'subaro', 'toyota', 'audi', 'audi', 'toyota']
print(cars)

# cars.sort()
# print(cars)

# cars.sort(reverse = True)
# print(cars)

# print(sorted(cars)) # temporary sorting
# print(cars)

# cars.reverse()
# print(cars)

print('Total number of cars : ',len(cars))
print('Total number of cars : %s'% (len(cars)))

print(cars[-1])
print(cars[-2])
print(cars[0:3])
print(cars[2:5])
print(cars[3:])
print(cars[:4])

print(cars.index('audi'))
print(cars.index('toyota'))

print('Toyota ache : ',cars.count('toyota'))
print('Audi ache : ',cars.count('audi'))

print(type(cars))
print(dir(cars))

cars.extend(['bmw', 'audi', 'subaro', 'toyota', 'audi', 'audi', 'toyota'])
print(cars)

gari = cars.copy()
print(gari)

gari.clear()
print(gari)