#Chat GPT utils correction
def days_in_month(month, year):
    """Return the number of days in a given month of a specific year."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    return 28

def get_month_list(year):
    """Return a list of dictionaries with months and their respective days for a specific year."""
    months_list = []
    for i in range(1, 13):
        month_dict = {
            "month": i,
            "days": days_in_month(i, year)
        }
        months_list.append(month_dict)
    
    return months_list
