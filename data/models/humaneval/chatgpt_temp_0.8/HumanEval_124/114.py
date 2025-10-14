def valid_date(date):
    # Step 1: Check if date string is not empty
    if not date:
        return False
    
    # Step 2: Parse the date string to extract the month, day and year values
    month, day, year = date.split('-')
    
    # Step 3: Check if the month value is between 1 and 12
    if not (1 <= int(month) <= 12):
        return False
    
    # Step 4: Check if the day value is valid for the given month and year
    days_in_month = {
        1: 31,
        2: 28 if int(year) % 4 != 0 or (int(year) % 100 == 0 and int(year) % 400 != 0) else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    if not (1 <= int(day) <= days_in_month[int(month)]):
        return False
    
    # Step 5: Return True if all checks pass
    return True
