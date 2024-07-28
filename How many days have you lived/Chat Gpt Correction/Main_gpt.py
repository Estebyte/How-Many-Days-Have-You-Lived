import utils

class Date:
    """Class to represent a date and calculate the day of the year."""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_the_year(self):
        """
        Como lo hice yo:  
                              
            Incrementa un contador por cada iteración del dia del año 
            hasta que coincide con la fecha de los parametros. 
            Luego se retorna el contador que será el numero del dia del año

            month_counter = 0
            days_counter = 0
            months_list = utils.get_month_list(self.year)

            for i in months_list:
                if i["month"] != self.month + 1:
                    month_counter += 1
                for y in range(1, i["days"] + 1 ): 
                    days_counter += 1
                    if month_counter == self.month and y == self.day:
                        return days_counter
        """
        """
        Como lo hizo chat gpt:
        Calculate the day of the year for the given date.
        """
        days_counter = 0
        months_list = utils.get_month_list(self.year)

        for i in months_list:
            if i["month"] < self.month:
                days_counter += i["days"]
            elif i["month"] == self.month:
                days_counter += self.day
                break
        
        return days_counter

def subtract_dates(year1, day_of_the_year1, year2, day_of_the_year2):
    """
    Calculate the number of days between two dates, considering leap years.
    """
    days_in_year = 365
    days_left_in_year1 = days_in_year - day_of_the_year1
    spare_days_in_year2 = day_of_the_year2
    years_between = year2 - year1 - 1
    total_days = days_left_in_year1 + spare_days_in_year2 + (years_between * days_in_year)

    return total_days

def main():
    birth = Date(2023, 7, 28)
    today = Date(2024, 7, 28) 

    total_days = subtract_dates(birth.year, birth.day_of_the_year(), today.year, today.day_of_the_year())
    print(f"You have lived {total_days} days!")

if __name__ == "__main__":
    main()