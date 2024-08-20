def is_leap(year):
    # Returns True or False if the year is or isn't leap.
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
    
def days_in_month(month, year):
    # Establishes the days in the months.
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        #Lap year logic
        if is_leap(year):
            return 29
        else:
            return 28

def days_in_year(year):
    # Establishes the days in the year.
    if is_leap(year):
        return 366
    else:
        return 365

def get_month_list(year):
    # Return a list of dictionaries with months and their respective days.
    months_list = []
    for i in range(1, 13):
        month_dict = {
            "month" : i,
            "days" : days_in_month(i, year)
        }
        months_list.append(month_dict)
    
    return months_list
    
if __name__ == "__main__":
    # Test the function.
    months_list = get_month_list(2024) 
    print(months_list)