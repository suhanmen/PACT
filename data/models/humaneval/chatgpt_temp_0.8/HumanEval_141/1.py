import re

def file_name_check(file_name):
    # Regular expression pattern for the file name validation
    pattern = '^[a-zA-Z][a-zA-Z0-9]*[.](txt|exe|dll)$'
    
    # Check if the file name matches the pattern
    if re.match(pattern, file_name):
        # Count the number of digits in the file name
        num_digits = sum(1 for c in file_name if c.isdigit())
        
        # Check if there are more than three digits
        if num_digits <= 3:
            return 'Yes'
    
    return 'No'
