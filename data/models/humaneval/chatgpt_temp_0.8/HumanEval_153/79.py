def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_ext = ''
    for extension in extensions:
        CAP = sum(1 for letter in extension if letter.isupper())
        SM = sum(1 for letter in extension if letter.islower())
        strength = CAP - SM
        if strength > max_strength:
            max_strength = strength
            strongest_ext = extension
    return class_name + '.' + strongest_ext
