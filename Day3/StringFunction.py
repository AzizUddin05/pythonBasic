msg = "Have a nice daY"
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg.swapcase())
print(msg.center(50))
print(msg.center(50,'*'))
print(msg.replace('nice','good'))
print(msg.find('nice'))
print(msg.find('day'))
print(msg.find('daY'))
print(msg.count('e'))
print(msg.startswith('h'))
print(msg.startswith('H'))
print(msg.endswith('y'))
print(msg.endswith('Y'))
print(msg.split())

word=msg.split()
print(word)
print(word[3])
print(word[2])

print(dir(msg))
print(type(msg))

x=10
print(type(x))
print(dir(x))