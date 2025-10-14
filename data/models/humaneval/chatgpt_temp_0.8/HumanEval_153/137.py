def Strongest_Extension(class_name, extensions):
    max_strength = float("-inf")
    strongest_extension = ""
    for extension in extensions:
        cap_count = sum(1 for letter in extension if letter.isupper())
        sm_count = sum(1 for letter in extension if letter.islower())
        strength = cap_count - sm_count
        if strength > max_strength or (strength == max_strength and extensions.index(extension) < extensions.index(strongest_extension)):
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
