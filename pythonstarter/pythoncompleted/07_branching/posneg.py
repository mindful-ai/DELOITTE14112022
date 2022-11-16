# Program to tell if the result was positive, negative or zero
# after subtraction of two numbers

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


# process
res = a - b

# output
print("-"*50)
print("DIFFERENCE  : ", abs(a - b))

# ---------- print results here with if..else.. block

if(res > 0):
    print("The result is positive")
elif(res < 0):
    print("The number is negative")
else:
    print("The number is zero")