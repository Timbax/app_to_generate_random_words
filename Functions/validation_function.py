def data_validation_in_words(max_length_param, min=3, max=10):
    while True:
        try:
            number_validation = max_length_param
            if number_validation < min:
                print(f"Error: El numero debe ser al menos {min}")
                break
            if max and number_validation > max:
                print(f"Error: El numero no puede ser mayor a {max}")
                break
            return number_validation
        except ValueError:
            print("Error: Por favor ingresa un número valido")


def data_validation_in_list_words(max_list_param, min=3, max=11):
    while True:
        try:
            number_list_validation = max_list_param
            if number_list_validation < min:
                print(f"Error: El numero de la lista debe ser al menos {min}")
                break
            if max and number_list_validation > max:
                print(f"Error: El numero de la lista no puede ser mayor a {max}")
                break
            return number_list_validation
        except ValueError:
            print("Error: Por favor ingresa un numero valido")