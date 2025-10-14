def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_ext = ""
    for extension in extensions:
        cap_letters = sum(1 for c in extension if c.isupper())
        sm_letters = sum(1 for c in extension if c.islower())
        strength = cap_letters - sm_letters
        if strength > max_strength:
            max_strength = strength
            strongest_ext = extension
    return f"{class_name}.{strongest_ext}"
