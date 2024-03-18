a = 100
b = 100 + 100
c = a + a 
d = b

print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))

if d is c:
    print('d is c', end=' : ')
if d is b:
    print('d is b')
