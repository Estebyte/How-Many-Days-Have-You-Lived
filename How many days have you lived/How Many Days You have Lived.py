import utils

def main():
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

        days_left = 365 - day_of_the_year1
        spare_days = day_of_the_year2
        years_substraction = (year2 - (year1 + 1))

        total = days_left + spare_days + (years_substraction * 365)
        return total
     
    birth = Date(2023, 7, 28)
    today = Date(2024, 7, 28) 

    total_days = substract_dates(birth.year, birth.day_of_the_year(), today.year, today.day_of_the_year())
    print(f"You have lived {total_days} days!")
      
main()