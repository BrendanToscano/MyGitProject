# Python program to check if the user input is a prime number.

# Ask user for number.
# Keep a loop
# If user is done with program exit.
# Catch errors.
while(true):
    try:
        print("1. If you want to check if a prime number.")
        print("2. If you want to exit program.")
        choice = input("Enter choice: -")
        
        # Choice menu
        if choice == 1:
            num = int(input("Enter number: -"))
            ###### Teammate 2 would proceed from here. ######
            ###### Since team was not involved I will do this part #####
            # Check if number is prime by using %.
                if i <= 1:
                    isPrime = False
                else:
                    for j in range(2, i-1):
                        if i % j == 0:
                            isPrime = False
                            break
                if isPrime:
                    print(f"{i} is a prime number.")
                else:
                    print(f"{i} is not a prime number.")
        elif choice == 2:
            print("Program ended successfully.")
            break
        else:
            print("Program ended unsuccessfully.")
            break
            
        
        
    except as e:
        print("{e}")


