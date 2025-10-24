try:
    limit = int(input("Enter a number: "))
    odd_numbers = [num for num in range(1, limit) if num % 2 != 0]
    print(f"List of odd numbers under {limit}: {odd_numbers}")
except ValueError:
    print("Invalid input. Please enter an integer.")