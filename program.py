from Utils.getOptionExpiryDate import getWeekEndingDayDate;
from Enums.optionExpiryDays import OptionExpiryDays;


#Current Week
print( getWeekEndingDayDate(OptionExpiryDays.Monday.value, 0))
print( getWeekEndingDayDate(OptionExpiryDays.Wednesday.value, 0))
print( getWeekEndingDayDate(OptionExpiryDays.Friday.value, 0))

#Next Week
print( getWeekEndingDayDate(OptionExpiryDays.Monday.value, 1))
print( getWeekEndingDayDate(OptionExpiryDays.Wednesday.value, 1))
print( getWeekEndingDayDate(OptionExpiryDays.Friday.value, 1))