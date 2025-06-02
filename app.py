from Functions.generate_words import generate_word_list
from Functions.input_validations import get_valid_number

def run_app():
    print("=== Random Word Generator ===\n")
    
    # Get user parameters
    max_length = get_valid_number(
        "Enter the maximum word length (3-15): ", 
        min=3, 
        max=15
    )
    
    max_list_words = get_valid_number(
        "Enter the number of words to generate: ", 
        min=3
    )
    
    # Generate and show the words
    print(f"\nGenerating {max_list_words} words(s) with maximum {max_length} letters:\n")
    
    word_list = generate_word_list(max_list_words, max_length)
    
    for i, palabra in enumerate(word_list, 1):
        print(f"{i}. {palabra}")

run_app()