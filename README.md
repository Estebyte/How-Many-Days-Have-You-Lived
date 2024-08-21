# How many Days Have You Lived

A Python script which calculates how many days have you lived since your date of birth to the current date WITHOUT USING PYTHON'S "datetime" LIBRARY.

## Instalation and Running the Script

To start using the program, you need to clone the repository and have [Python](https://www.python.org/) installed on your system.

1. Clone the repository

```bash
git clone https://github.com/Estebyte/How-Many-Days-Have-You-Lived.git
```

2. Navigate to the project directory

```bash
cd How-Many-Days-Have-You-Lived
```

3. Run the script

```bash
python3 main.py
```

## Substraction Explication

The substraction algorithm works as follows:

1. The birth date is adjusted to the first day of the next year, and the current date is adjusted to the first day of its respective year. The differences in days between the original dates and these new dates are stored in two variables. days_left, the days left to the end of the birth year, and spare_days, the days that have passed in the current year.

3. Next, a for loop is used to count the days between these "new dates" and the result is stored in a new variable, days_between_years.

4. The final result is the sum of days_left, days_between_years, and spare_days.

## Contributing

Pull request are welcome. I'm a student, and I'm open to any contributions or sugestions.
