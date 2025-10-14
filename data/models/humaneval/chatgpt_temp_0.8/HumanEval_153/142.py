def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    strongest_strength = float('-inf')
    
    for ext in extensions:
        cap = sum(1 for letter in ext if letter.isupper())
        sm = sum(1 for letter in ext if letter.islower())
        strength = cap - sm
        if strength > strongest_strength:
            strongest_extension = ext
            strongest_strength = strength
    
    return f"{class_name}.{strongest_extension}"
