def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    strongest_strength = float('-inf')
    
    for ext in extensions:
        cap_count = sum(1 for c in ext if c.isupper())
        sm_count = sum(1 for c in ext if c.islower())
        strength = cap_count - sm_count
        
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    
    return class_name + '.' + strongest_ext
