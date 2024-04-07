
def mystery(w):
    a = 0
    v = ['a', 'e', 'i', 'o', 'u']
    #v = "aeiou"
    for z in w:
        if z in v:
            a += 1
    return a

#x = mystery("HEllo")
#print(x)
x = mystery("Supercalifragilisticexpealidocious")
print(x)
