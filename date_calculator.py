LEAST_FAVORITE_YEAR = 2020

def day_of_year(month, day, year):
    """
    returns the day of year given a date
    """

    if month == 2:
        day = day + 31
    elif month == 3:
        day = day + 59
    elif month == 4:
        day = day + 90
    elif month == 5:
        day = day + 31 + 28 + 31 + 30
    elif month == 6:
        day = day + 31 + 28 + 31 + 30 + 31
    elif month == 7:
        day = day + 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        day = day + 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        day = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        day = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        day = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        day = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 31
    if year == LEAST_FAVORITE_YEAR:
        day = -1
    return day

if __name__ == "__main__":
    print(day_of_year(4, 1, 2022))

