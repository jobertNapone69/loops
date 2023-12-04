def smallest_factor(bert):
    if bert < 10:
        print("Invalid input. Enter a number greater than 10.")
        return None  # Stop the program if n is less than 10

    i = 2
    while i <= bert:
        if bert % i == 0:
            return i  # Return the smallest factor if it is found
        i += 1

    return bert  # Return n if it is a prime number


bert = int(input("Enter an integer greater than or equal to 10: "))  # Get the input from the user
smallest_factor = smallest_factor(bert)  # Call the function to find the smallest factor
if smallest_factor != bert:  # Check if n is a prime number
    print(f"The smallest factor other than 1 for {bert} is {smallest_factor}.")
else:
    print(f"{bert} is a prime number.")
