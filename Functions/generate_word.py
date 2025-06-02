import random


def generate_random_word(max_length_param):

    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
 
    word_length = random.randint(3, max_length_param)
 
    generate_word = ''
    begins_with_vowel = random.choice([True, False])
  
    for i in range(word_length):
        if (i % 2 == 0 and begins_with_vowel) or (i % 2 == 1 and not begins_with_vowel):
            generate_word += random.choice(vowels)
        else:
            generate_word += random.choice(consonants)
    
    return print(f"Random Word: {generate_word}") 


def generate_word_list(number_of_words_param, max_length_param):
    print("Valores dentro de la funcion number_of_words: ",number_of_words_param)
    print("Valores dentro de la funcion max_length_param: ",max_length_param)
    word_list = []
    for _ in range(number_of_words_param):
        print("Proceso recorrido :", word_list.append(generate_random_word(max_length_param)))
        #word_list.append(generate_random_word(max_length_param))

    return word_list




