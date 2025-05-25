import random

def generate_random_word(max_length_param):

    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
 
    word_length = random.randint(3, max_length_param)
 
    empty_word = ''

    begins_with_vowel = random.choice([True, False])
  
    for i in range(word_length):
        if (i % 2 == 0 and begins_with_vowel) or (i % 2 == 1 and not begins_with_vowel):
            empty_word += random.choice(vowels)
        else:
            empty_word += random.choice(consonants)
    
    return empty_word


def generate_word_list(number_of_words_param, max_length_param):
   
    word_list = []
    for _ in range(number_of_words_param):
        word_list.append(generate_random_word(max_length_param))
    return word_list