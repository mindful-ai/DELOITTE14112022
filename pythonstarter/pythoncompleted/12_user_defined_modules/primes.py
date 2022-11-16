# Write a function checkprime which returns True if the number is prime and False otherwise
def checkprime(x):
    prime = True
    for i in range(2, x):
        if(x % i == 0):
            prime = False
    return prime

print("primes.py __name__ => ", __name__)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if(checkprime(n) == True):
        print("The number is prime")
    else:
        print("The number is  not prime")


'''
n = int(input("Enter a number: "))
if(checkprime(n) == True):
    print("The number is prime")
else:
    print("The number is  not prime")
'''
