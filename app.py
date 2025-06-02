#from Functions.generate_word import generate_random_word
from Functions.generate_word import generate_word_list
from Functions.validation_function import data_validation_in_words
from Functions.validation_function import data_validation_in_list_words


print("IMPORTANT: Minimum 3 and maximum 10 letters.")

max_length = int(input("Enter the number for word length (3-10): "))
max_list_words = int(input("Enter the number of words you need: "))

longitud_maxima = data_validation_in_words(max_length)
print("Proceso de longitud maxima: ",longitud_maxima)

cantidad = data_validation_in_list_words(max_list_words)
print("Proceso de cantidad: ",cantidad)

palabras = generate_word_list(cantidad, longitud_maxima)
print("Proceso de palabras: ",palabras)

# def ejecutar_programa():

#     max_length = int(input("Enter the number for word length (2-9): "))
#     max_list_words = int(input("Enter the number of words you need: "))

#     longitud_maxima = data_validation_in_words(max_length)

#     cantidad = data_validation_in_list_words(max_list_words)

#     print(f"\nGenerando {cantidad} palabra(s) con máximo {longitud_maxima} letras:\n")

#     palabras = generate_word_list(cantidad, longitud_maxima)

#     for i, palabra in enumerate(palabras, 1):
#         print(f"{i}. {palabra} ({len(palabra)} letras)")


# ejecutar_programa()



#new_random_word = generate_random_word(max_length)

#print(f"\nGenerando {max_words} palabra(s) con máximo {max_length} letras:\n")

#new_word_list = generate_word_list(max_words, max_length)


