def Strongest_Extension(class_name, extensions):
    strength_dict = {}
    for extension in extensions:
        cap_letters = sum(1 for letter in extension if letter.isupper())
        sm_letters = sum(1 for letter in extension if letter.islower())
        strength = cap_letters - sm_letters
        strength_dict[extension] = strength
    strongest_extension = sorted(strength_dict.items(), key=lambda x: (x[1], extensions.index(x[0])))[0][0]
    return f"{class_name}.{strongest_extension}"
