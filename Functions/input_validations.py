def get_valid_number(message, min=3, max=15):
    while True:
        try:
            number = int(input(message))
            if number < min:
                print(f"Error: The number must be at least {min}")
                continue
            if max and number > max:
                print(f"Error: The number cannot be bigger than {max}")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid number")