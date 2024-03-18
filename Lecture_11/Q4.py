total = 0
# LCV is x, initial value is user input
x = int(input("Enter a value: "))
# requirement 4: x <= 0 will end the loop
while x > 0:
    total += x
    # req 3: get a new value for LCV
    x = int(input("Enter a value: "))
print(f"Total: {total}")
