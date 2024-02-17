phrase = input("Enter greeting: ")

# Test for initial cap Hello
if phrase == "Hello":
    print("First", end=" ")
    
# Test for all caps HELLO with else
if phrase == "HELLO":
    print("Second", end=" ")
else:
    print("Third")
