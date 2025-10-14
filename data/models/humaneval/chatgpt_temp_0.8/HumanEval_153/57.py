def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = float('-inf')
    
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
            
    return f"{class_name}.{strongest_extension}"
