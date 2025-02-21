def days_passed_since_birth(birthday):
    #Extract the birth year from the string
    birth_year = int(birthday.split("-")[2])  #Extract "YYYY" and convert to int

    #Assume current year is 2025
    current_year = 2025

    #Exclude current and birth year
    full_years = (current_year - birth_year) - 1

    #Count leap years
    leap_years = 0
    for year in range(birth_year + 1, current_year):  #Check full years only
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1  # Add leap year count

    #Calculate how many days
    total_days = (full_years * 365) + leap_years  #normal days + leap year days

    return total_days

#Test it out
print(days_passed_since_birth("08-07-2005"))
