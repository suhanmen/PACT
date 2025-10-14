def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
        
    # Split the date into its components
    try:
        month, day, year = map(int, date.split("-"))
    except ValueError:
        return False
        
    # Check if the month is valid (between 1 and 12)
    if month < 1 or month > 12:
        return False
        
    # Check if the day is valid for the given month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        max_day = 29
    else:
        max_day = 28
        
    if day < 1 or day > max_day:
        return False
        
    # Check if the year is valid (between 1 and 9999)
    if year < 1 or year > 9999:
        return False
        
    # Check if the date is in the correct format
    if not date.isdigit() or len(date) != 10 or date[2] != "-" or date[5] != "-":
        return False
   
