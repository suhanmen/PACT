def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_extension = None
    
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    
    return f"{class_name}.{strongest_extension}"
