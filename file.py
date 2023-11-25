'''
NOTE: open function

file = open('text.txt', 'r')
content = file.read()
print(content)
file.close()
'''

'''
NOTE: with statement, it auto close the file
 - Automatic resource management
 - Cleaner and more concise code

with open('text.txt', 'r') as file:
    content = file.read()
    print(content)

'''

'''
NOTE: read lines, can be called multiple times to read subsequent lines


'''
with open('text.txt', 'r') as file:
    for line in file.readlines():
        print(line)