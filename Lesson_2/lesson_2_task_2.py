def is_year_leap(year):
    if (year % 4 == 0):
        return(f"год {year}: True")
    else:
        return(f"год {year}: False")

random_year = is_year_leap(2023)
print(random_year)