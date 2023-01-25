def is_leap(year):
    leap = False

    if year % 4:
        leap = False
    else:
        if year % 100:

            leap = True
        else:
            if year % 400:
                leap = False
            else:
                leap = True
    
    return leap

year = int(input())
print(is_leap(year))