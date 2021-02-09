# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Example: s = '12:01:00PM' >> '12:01:00'
#          s = '12:01:00AM' >> '00:01:00'

def ConversionTime():

    s = "08:05:45AM"
    newPMhour = ''
    newAMhour = ''
    AM_PM = s[-2:] # AM or PM

    if AM_PM == 'AM':
        FullHour = s.replace('AM', '') # 12:05:45PM  >> 12:05:45
        getHour = s[:2] # 12
        if int(getHour)==12:
            newAMhour = FullHour.replace('12', '00')
            print(newAMhour)
        else:
            newAMhour = FullHour
            print(newAMhour)
    else: # PM
        FullHour = s.replace('PM', '')
        getHour = s[:2]
        if int(getHour)==12:
            newPMhour = FullHour
            print(newPMhour) # 12:05:45
        else:
            getNewHour = int(FullHour[:2]) # 05-06-07-08-09
            getMinSec = FullHour[2:] # :05:45
            getNewHour = getNewHour + 12 # 07 + 12 = 19
            newPMhour = str(getNewHour) + getMinSec # 20:05:45
            print(newPMhour) 


ConversionTime()