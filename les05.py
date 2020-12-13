import sys

print(sys.version, sys.platform)
a = 5
b = 1.25
c = 'Hello world!'
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

lst = [l for l in range(10)]
