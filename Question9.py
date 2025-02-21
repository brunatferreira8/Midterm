def days_passed_since_birth(birthday):
    # Step 1: Extract the birth year from the string
    birth_year = int(birthday.split("-")[2])  # Extract "YYYY" and convert to int

    #Assume current year is 2025
    current_year = 2025

    #Exclude current and birth year
    full_years = (current_year - birth_year) - 1

    #Count leap years
    leap_years = 0
    for year in range(birth_year + 1, current_year):  #Check full years only
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1  # Increment leap year count

    # Step 5: Total days calculation
    total_days = (full_years * 365) + leap_years  # Regular days + leap year days

    return total_days


# Example Usage
print(days_passed_since_birth("15-08-2000"))  # Example birth date
