# Program to get the number inputs from the user and finding the average of the numbers

'''
INPUT <- 10 20 30 40 50 60
OUTPUT -> 35

'''

# input
n = input("Enter the numbers separated by spaces: ")

# process
x = n.split()
p = []
for item in x:
    p.append(int(item))

# output
print("Average = ", sum(p)/len(p))