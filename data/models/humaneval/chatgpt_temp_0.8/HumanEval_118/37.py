def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    # Convert word to lowercase
    word = word.lower()

    # Get the consonants from the right side of the word
    consonants = ""
    for i in range(len(word)-1, -1, -1):
        if word[i] not in "aeiou":
            consonants = word[i] + consonants
        else:
            break

    # Get the closest vowel between two consonants from the right side
    for i in range(len(consonants)-1):
        if consonants[i] not in "aeiou" and consonants[i+1] in "aeiou":
            return consonants[i+1]

    # If no vowel was found, return empty string
    return ""
