names = []
n = input("Enter name: ")
while n != "done":
    names.append(n)
    n = input("Enter name: ")
names.sort(reverse=True, key=str.upper)
print(names)
