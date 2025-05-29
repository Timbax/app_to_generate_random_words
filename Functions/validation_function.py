def data_validation_in_words(max_length_param, min=3, max=10):
    while True:
        try:
            number_validation = max_length_param
            if number_validation < min:
                print(f"Error: El número debe ser al menos {min}")
                continue
            if max and number_validation > max:
                print(f"Error: El número no puede ser mayor a {max}")
                continue
            return number_validation
        except ValueError:
            print("Error: Por favor ingresa un número válido")


def data_validation_in_list_words(max_list_param, min=3, max=11):
    while True:
        try:
            number_list_validation = max_list_param
            if number_list_validation < min:
                print(f"Error: El número de la lista debe ser al menos {min}")
                continue
            if max and number_list_validation > max:
                print(f"Error: El número de la lista no puede ser mayor a {max}")
                continue
            return number_list_validation
        except ValueError:
            print("Error: Por favor ingresa un número válido")