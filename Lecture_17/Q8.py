def fun1(num):
    return num + 25

def fun2(a, b):
    return fun1(a) + fun1(b)

def main():
#     print(fun2(30, 20))
    print(fun2(10,20))

if __name__ == '__main__':
    main()
