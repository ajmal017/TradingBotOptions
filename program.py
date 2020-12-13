from Utils.getOptionExpiryDate import getOptionExpiryDate;
from Enums.optionExpiryDays import OptionExpiryDays;


#Current Week
print( getOptionExpiryDate(OptionExpiryDays.Monday.value, 0))
print( getOptionExpiryDate(OptionExpiryDays.Wednesday.value, 0))
print( getOptionExpiryDate(OptionExpiryDays.Friday.value, 0))

#Next Week
print( getOptionExpiryDate(OptionExpiryDays.Monday.value, 1))
print( getOptionExpiryDate(OptionExpiryDays.Wednesday.value, 1))
print( getOptionExpiryDate(OptionExpiryDays.Friday.value, 1))