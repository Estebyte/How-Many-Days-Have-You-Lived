import utils

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_the_year(self):
        # Calculate the day of the year for the given date, summing the days of the month to a counter.
        days_counter = 0
        months_list = utils.get_month_list(self.year)

        for i in months_list:
            if i["month"] < self.month:
                days_counter += i["days"]
            elif i["month"] == self.month:
                days_counter += self.day
                break
        return days_counter

def substract_dates(birth, current_date):
    # Days left to end the birth year.
    days_left = utils.days_in_year(birth.year) - birth.day_of_the_year() 

    # Days that have passed after the start of the current year.
    spare_days = current_date.day_of_the_year() 

    # Total days in the full years between the two "new dates".
    # The for loop skips counting the birth year and the current year since those days are handled separately.
    days_between_years = 0
    for year in range(birth.year + 1, current_date.year): 
        days_between_years += utils.days_in_year(year)

    total = days_left + days_between_years + spare_days 
    return total
    
    # For more details on how the subtraction algorithm works, refer to the README.md 

def main():
    #Ask the user for his birth data and the current date
    birth_year, birth_month, birth_day = map(int, input("Enter your birth in YYYY/MM/DD format: ").split("/"))
    birth = Date(birth_year, birth_month, birth_day)

    current_year, current_month, current_day = map(int, input("Enter the current date in YYYY/MM/DD format: ").split("/"))
    current_date = Date(current_year, current_month, current_day) 

    #Substract Dates
    total_days = substract_dates(birth, current_date)

    #Print the result
    print(f"You have lived {total_days} days!")

if __name__ == "__main__":
    main()