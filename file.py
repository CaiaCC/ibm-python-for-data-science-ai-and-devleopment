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

with open('text.txt', 'r') as file:
    for line in file.readlines():
        print(line)
'''


'''
NOTE: write file with open()

lines = ['this is line #1\n', 'this is line #2\n', 'this is line #3\n']

with open('text-for-writing.txt', 'w') as file:
    for line in lines:
        file.write(line)
'''

'''
NOTE: appending data to an existing file


'''

new_data = 'this is the new line'

with open('text-for-writing.txt', 'a') as file2:
    file2.write(new_data +)