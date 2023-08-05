def is_leap(year):
    leap = False
    
    # Logic --> For a year to be a leap year it must be:
    #         1. Divisible/Multiple by 400.
    #         2. Divisible/Multiple of 4 and not Divisible/Multiple of 100.
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return True
    else:
        return False
    
    return leap

year = int(input())
print(is_leap(year))