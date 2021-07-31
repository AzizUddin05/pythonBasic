"""
Syntax to open the file

file object = open("file name", "mode")

'r' - read mode
'w' - write mode
'A' - Append mode
'r+' - Read/Write mode
"""
# Open a file for write mode
file = open("pyBatch6.txt", "w")
file.write("Hello World !")
file.write("This is our new text file")
file.write("And this is another line")
file.write("This is write mode")

file.write("\nHello World !\n")
file.write("This is our new text file\n")
file.write("And this is another line\n")
file.write("This is write mode\n")

file.close()

# Open a file for read mode
file = open("pyBatch6.txt", "r")

# Read Entire file
# print(file.read())
# print(file.read(8))
# print(file.read(16))
# print(file.readline()) # readline = reads only one line
print(file.readlines()) # for read all line by coma seperated
file.close()

file = open("pyBatch6.txt", "r")
s = file.readlines()
for line in s:
    print(line)
file.close()

file = open("pyBatch6.txt", "r")
# s = file.readlines()
for line in file:
    print(line)
file.close()

file = open("pyBatch6.txt", "a")
file.write("\nWe meet again\n")
file.write("Python is awesome\n")
file.close()

file = open("pyBatch6.txt", "r")
for line in file:
    print(line)
file.close()

i = 1
file = open("pyBatch6.txt", "r")
for line in file:
    print(i, '-', line)
file.close()
