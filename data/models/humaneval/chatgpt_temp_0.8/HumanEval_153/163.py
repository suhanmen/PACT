def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_ext = None
    
    for ext in extensions:
        cap_count = len([c for c in ext if c.isupper()])
        sm_count = len([c for c in ext if c.islower()])
        strength = cap_count - sm_count
        
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    
    return f"{class_name}.{strongest_ext}"
