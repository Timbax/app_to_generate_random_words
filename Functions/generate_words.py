import random

def generate_random_word(longitud_maxima):
   
    # We define vowels and consonants
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # We choose a random length between 3 and the maximum
    word_length = random.randint(3, longitud_maxima)
    
    # Iniciamos con una palabra vacía
    generate_word = ''
    
    # Decidimos aleatoriamente si empezamos con vocal o consonante
    begins_with_vowel = random.choice([True, False])
    
    # We build the word alternating between vowels and consonants
    for i in range(word_length):
        if (i % 2 == 0 and begins_with_vowel) or (i % 2 == 1 and not begins_with_vowel):
            generate_word += random.choice(vowels)
        else:
            generate_word += random.choice(consonants)
    
    return generate_word

def generate_word_list(quantity_param, maximum_length_param):
    
    words = []
    for _ in range(quantity_param):
        words.append(generate_random_word(maximum_length_param))
    return words