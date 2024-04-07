def mystery(w):
    a = 0
    v = ['a', 'e', 'i', 'o', 'u']
    for z in w:
        if z in v:
            a += 1
    return a

x = mystery("Whatever")
print(x)
