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
    vowels = set("aeiouAEIOU")
    idx = len(word) - 2
    while idx > 0:
        if word[idx] in vowels:
            for i in range(idx-1, 0, -1):
                if word[i] not in vowels:
                    return word[idx]
            return ""
        idx -= 1
    return ""
