def most_frequent(input_string):
    # Initialize an empty dictionary to store letter frequencies
    letter_freq = {}
    
    # Calculate letter frequencies
    for letter in input_string:
        if letter.isalpha():  # Check if the character is a letter
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
    
    # Sort the dictionary by values in descending order
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Print letters in decreasing order of frequency
    for item in sorted_letter_freq:
        print(f"{item[0]} = {item[1]:02d}")

# Example usage:
input_string = "Mississippi"
most_frequent(input_string)
