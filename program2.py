# Python program to check if the user input is a prime number.

# Ask user for number.
# Keep a loop
# If user is done with program exit.
# Catch errors.
while(true):
    try:
        print("1. If you want to check if a prime number.")
        print("2. If you want to exit program.")
        choice = int(input("Enter choice: -"))
        
        if choice == 1:
            num = int(input("Enter number: -"))
            # Check if number is prime by using %.
        
    except as e:
        print("{e}")


