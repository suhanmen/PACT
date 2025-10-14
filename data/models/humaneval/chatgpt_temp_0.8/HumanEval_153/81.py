def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strengths[ext] = cap - sm
    
    strongest = max(strengths.items(), key=lambda x: x[1])
    strongest_ext = strongest[0]
    
    return f"{class_name}.{strongest_ext}"
