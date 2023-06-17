year = int(input('write a year '))
tmp = year - 1600
leap_years = (tmp) // 4 - (tmp) // 100 + (tmp) // 400 + 1
print(leap_years)
