# Python program to display all the prime numbers within an interval.

# Ask user for interval.
# Catch errors.
while True:
    try:
        startNum = int(input("Enter a starting range:- "))
        endNum = int(input("Enter a ending range:- "))
        break;
    except:
        print("Input was invalid.")

# Run through all numbers in given range.
for i in range(startNum, endNum + 1):
    ###### Teammate 1 was suppose to do this part. ######
    ###### Since team was not involved I will do this part #####
    # Check if the all numbers in the range are prime or not.
    isPrime = True
    if i <= 1:
        isPrime = False
    else:
        for j in range(2, i-1):
            if i % j == 0:
                isPrime = False
                break
    
    # If number is prime print it.
    if isPrime:
        print(f"{i} \n")
