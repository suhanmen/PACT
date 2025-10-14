def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_extension = ''
    for extension in extensions:
        cap = sum(1 for letter in extension if letter.isupper())
        sm = sum(1 for letter in extension if letter.islower())
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
