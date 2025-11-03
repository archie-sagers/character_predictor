import pandas as pd

input_file = "dictionary_extract.txt"

# Function to get a sorted dictionary with the frequency of used letters in text file
def full_character_dictionary(filename):
    """Returns sorted dictionary with frequency of used letters in text file"""
    char_dict = {}
    with open(input_file) as f:
        text = f.read().lower()
        
    # Assigns the current character and the frequency of a following character to variables
    for i in range(len(text)-1):
        current = text[i]
        nxt = text[i + 1]

        # Check both current and next characters are valid and add to dictionary if not already in
        if current.isalpha() and nxt.isalpha():
            if current not in char_dict:
                char_dict[current] = {}

            # Add the following character to the dictionary and increase the value for each occurance
            if nxt not in char_dict[current]:
                char_dict[current][nxt] = 1
            else:
                char_dict[current][nxt] += 1
                
    # Sorts the dictionary of dictionaries by the frequency of character occurance
    for key in char_dict:
        char_dict[key] = dict(sorted(char_dict[key].items(), key=lambda x: x[1], reverse=True))

    # Sorts the dictionary alphabetically 
    sorted_char_dict = dict(sorted(char_dict.items()))
    
    return sorted_char_dict

sort_char_dict = full_character_dictionary(input_file)

user_ch = input('please enter your character and I will predict the next: ')

def predicter(user_ch):
    """Takes user input and predicts the next character using input file"""
    final_ch = user_ch[-1].lower()
    if final_ch in sort_char_dict:
        sub_dict = sort_char_dict[final_ch]
        # Grabs the top key from the sub dictionary (it's already sorted by frequency by the function that created it)
        top_key = next(iter(sub_dict))
        return top_key

print(user_ch + predicter(user_ch))
    