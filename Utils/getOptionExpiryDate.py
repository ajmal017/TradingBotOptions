from datetime import date;
#TODO can be combine together   
import datetime;
from Enums.optionExpiryDays import OptionExpiryDays;

DEFAULT_DATE_FROMAT = 'YYYYMMDD'

today = date.today();

def getTodaysDate():
    return today;

def getTodaysDate(format = DEFAULT_DATE_FROMAT):
    #TODO Add Cases if needed
    return today.strftime("%Y%m%d")

def formatDate(date, format = DEFAULT_DATE_FROMAT):
    return date.strftime("%Y%m%d")

def getWeekEndingDayDate(day = OptionExpiryDays.Monday, weeks = 0):
    expiryDate = today + datetime.timedelta(days = -today.weekday() + day, weeks = weeks)
    return formatDate(expiryDate)
