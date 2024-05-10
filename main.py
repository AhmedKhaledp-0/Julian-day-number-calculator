def get_the_UT():
    hour = int(input("Enter the hour : "))
    if not (hour >= 1 and hour <= 24):
        raise ValueError (f"{hour} is not valid . The hour should be between 1 & 24")
    minute = int(input("Enter the minute : "))
    if not (minute >= 1 and minute <= 60):
        raise ValueError (f"{minute} is not valid . The minute should be between 1 & 60")
    second = int (input("Enter the second : "))
    if not (second >= 1 and second <= 60):
        raise ValueError (f"{second} is not valid . The second should be between 1 & 60")
    return (hour, minute, second)

def calculate_at_specific_UT(Julian_day, hour, minute, second):
    ut_in_hours = hour + (minute / 60) + (second / 3600)
    Julian_day_ut = round(Julian_day + ut_in_hours /24 ,3)
    print (f"\nJD = {Julian_day} + {ut_in_hours / 24}")
    print (f"\nJD = {Julian_day_ut}")

def main():

    #get the date input & check if it is  true
    year_date = int(input("Enter the year : "))
    if not (year_date >= 1901 and year_date <= 2099):
        raise ValueError (f"{year_date} is not valid . The Year should be between 1901 & 2099 ")

    month_date = int(input("Enter the month : "))
    if not (month_date >= 1 and month_date <= 12):
        raise ValueError (f"{month_date} is not valid . The month should be between 1 & 12")

    day_date = int(input("Enter the day : "))
    if not (day_date >= 1 and day_date <= 31):
        raise ValueError (f"{day_date} is not valid . The day should be between 1 & 31")
    x = month_date
    if ( x == 4  or x == 6 or x == 9 or x == 11 ) and day_date == 31:
        raise ValueError (f"Month {month_date} is just 30 day")
    elif  x == 2:
        if  day_date == 29 and year_date % 4 != 0 :
            raise ValueError (f"Month {month_date} is just 28 day")
        elif day_date > 29:
            raise ValueError (f"Month {month_date} is just 29 day")
        
    #calculate the Julian day number Jo
    print (f"\n converting dd/mm/yy {day_date}/{month_date}/{year_date} to Julian day number at   UT = 0")
    Julian_day = (367 * year_date - int(((7 * (year_date + (int((month_date + 9) / 12)))) / (4) )) + int (275 * month_date/ 9) + day_date + 1721013.5)
    print (f"Jo = {367 * year_date} - {int(((7 * (year_date + (int((month_date + 9) / 12)))) / (4) ))} + {int (275 * month_date/ 9)} + {day_date} + {1721013.5}")
    print (f"Jo = {Julian_day} \n ")

    #Get the time at any UT
    at_specific_UT = input ("do you want to get the time at specific UT \n \t1 - Yes \n \t2- No\n")
    if at_specific_UT == "1":
        hour,minute, second = get_the_UT()
        calculate_at_specific_UT(Julian_day, hour, minute, second)
    elif at_specific_UT == "2":
        print("")
    else:
        raise ValueError("Not a valid input")

if __name__ == "__main__" :
    main()