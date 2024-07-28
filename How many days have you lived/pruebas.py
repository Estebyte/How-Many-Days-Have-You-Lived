import utils 

class Date:
    """Class to represent a date and calculate the day of the year."""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_the_year(self):
        """
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
    
    def day_of_the_year2(self):
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
    
def main():
    birth = Date(2023, 7, 27)
    today = Date(2024, 7, 27) 

    print(today.day_of_the_year())
    print(today.day_of_the_year2())

if __name__ == "__main__":
    main()