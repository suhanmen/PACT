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
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    word = word.lower()
    start_index = 1
    end_index = len(word) - 2
    for i in range(end_index, start_index - 1, -1):
        if word[i] in vowels:
            for j in range(i - 1, start_index - 1, -1):
                if word[j] not in vowels:
                    for k in range(i + 1, end_index + 1):
                        if word[k] not in vowels:
                            return word[i].upper()
    return ""
