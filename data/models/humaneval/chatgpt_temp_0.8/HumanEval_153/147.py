def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    strongest_strength = float('-inf')
    
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
            
    return f"{class_name}.{strongest_extension}"
