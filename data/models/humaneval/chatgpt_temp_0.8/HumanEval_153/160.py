def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_extension = ''

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
        elif strength == max_strength and extensions.index(extension) < extensions.index(strongest_extension):
            strongest_extension = extension

    return f'{class_name}.{strongest_extension}'
