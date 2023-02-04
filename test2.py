from os import listdir

a = listdir(path='.')
print(a)
a = listdir(path='users')
print(a)
f = open('users/users.txt')
print(f.readlines())