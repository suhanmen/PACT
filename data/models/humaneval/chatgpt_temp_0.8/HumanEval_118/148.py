def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u']) # set of vowels
    word = word.lower() # convert the word to lowercase to make it case-insensitive
    vowel_found = False # flag variable to check if a vowel was found
    
    for i in range(len(word)-2, 0, -1): # iterate from second-last character to second character
        if word[i] in vowels: # if character is a vowel
            vowel_found = True # set the flag variable as True
            break # exit the loop
        
        if word[i] not in vowels and word[i-1] in vowels and word[i+1] not in vowels: # if the current character is a consonant and the previous and next characters are vowels
            vowel_found = True # set the flag variable as True
            i -= 1 # go to the previous character
            break # exit the loop
    
    if vowel_found: # if a vowel was found
        return word[i] # return the vowel
    else:
        return "" # otherwise, return an empty string
