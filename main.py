import utils

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_the_year(self):
        #Calculate the day of the year for the given date.
        days_counter = 0
        months_list = utils.get_month_list(self.year)

        for i in months_list:
            if i["month"] < self.month:
                days_counter += i["days"]
            elif i["month"] == self.month:
                days_counter += self.day
                break
        return days_counter

def substract_dates(year1, day_of_the_year1, year2, day_of_the_year2):
    days_left = utils.days_in_year(year1) - day_of_the_year1
    spare_days = day_of_the_year2
    years_substraction = (year2 - (year1 + 1))

    total = days_left + spare_days + (years_substraction * 365)
    return total

def main():
    #Ask the user for his birth data and the current date
    birth_year, birth_month, birth_day = map(int, input("Enter your birth in YYYY/MM/DD format: ").split("/"))
    birth = Date(birth_year, birth_month, birth_day)

    current_year, current_month, current_day = map(int, input("Enter the current date in YYYY/MM/DD format: ").split("/"))
    current_date = Date(current_year, current_month, current_day) 

    #Substract Dates
    total_days = substract_dates(birth.year, birth.day_of_the_year(), current_date.year, current_date.day_of_the_year())

    #Print the result
    print(f"You have lived {total_days} days!")

if __name__ == "__main__":
    main()