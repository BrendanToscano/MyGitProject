# Python program to display all the prime numbers within an interval.

# Ask user for interval.
# Catch errors.
try:
    startNum = int(input("Enter a starting range:- "))
    endNum = int(input("Enter a ending range:- "))
except:
    print("Input was invalid.")

# Run through all numbers in given range.
for i in range(startNum, endNum):
    # Check if the all numbers in the range are prime or not.

    # If number is prime print it.
