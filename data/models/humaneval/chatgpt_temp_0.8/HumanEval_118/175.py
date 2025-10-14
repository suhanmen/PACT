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
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    first_cons = None
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i+1] not in vowels:
            first_cons = i
            break
    if first_cons is None:
        return ""
    else:
        for i in range(first_cons, len(word)):
            if word[i] in vowels:
                return word[i]
    return ""
