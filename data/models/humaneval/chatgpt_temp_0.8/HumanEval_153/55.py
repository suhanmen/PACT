def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_extension = ''
    for extension in extensions:
        CAP = len([char for char in extension if char.isupper()])
        SM = len([char for char in extension if char.islower()])
        strength = CAP - SM
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f'{class_name}.{strongest_extension}'
