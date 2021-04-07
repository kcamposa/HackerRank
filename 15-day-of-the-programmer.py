year = 1500

def dayOfProgrammer(year):
    if year >= 1700 and year <= 1917:
        # Julian Calendar
        print("Julian Calendar", year)
    elif year >= 1918:
        # Gregorian Calendar 
        print("Gregorian Calendar", year)

dayOfProgrammer(year)
