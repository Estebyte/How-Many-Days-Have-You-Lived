def days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28

def get_month_list(year):
    #Return a list of dictionaries with months and their respective days.
    months_list = []
    for i in range(1, 13):
        month_dict = {
            "month" : i,
            "days" : days_in_month(i, year)
        }
        months_list.append(month_dict)
    
    return months_list
    
if __name__ == "__main__":
    months_list = get_month_list(2024)
    print(months_list)