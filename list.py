"""
#  extend vs. append
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("l", l);
m = ['hello', 'world']
l.extend(m)
print("extended", l)

# deleting element in list
print('before: ', l)
del l[0]
print('after: ', l)

# split
s = 'hello there'.split()
print(s)

"""

# clone list
a = [1, 3, 9, 12]
b = a[:]

b[1] = 2

print(a)
print(b)