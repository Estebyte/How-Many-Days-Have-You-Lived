# Program Description
This program calculates the number of days between two dates without using Python's datetime library.

# Algorithm
The substraction algorithm works as follows:

1. The birth date is adjusted to the first day of the next year, and the current date is adjusted to the first day of its respective year. The differences in days between the original dates and these new dates are stored in two variables. days_left, the days left to the end of the birth year, and spare_days, the days that have passed in the current year.

3. Next, a for loop is used to count the days between these "new dates" and the result is stored in a new variable, days_between_years.

4. The final result is the sum of days_left, days_between_years, and spare_days.
