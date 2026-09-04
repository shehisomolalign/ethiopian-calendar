from datetime import date
from ethiopian_calendar import EthiopicDate

# 1. Create an Ethiopian date
eth_date = EthiopicDate(year=2015, month=1, day=1)
print("Ethiopian Date:", eth_date)  # Output: 1 Meskerem 2015
print("Amharic Month:", eth_date.month_name(lang="amharic"))  # Output: መስከረም

# 2. Convert Ethiopian date to Gregorian date
greg_date = eth_date.to_gregorian()
print("Gregorian Date:", greg_date)  # Output: 2022-09-11

# 3. Convert Gregorian date back to Ethiopian date
converted_eth = EthiopicDate.from_gregorian(date(2022, 9, 11))
print("Converted back:", converted_eth)  # Output: 1 Meskerem 2015

# 4. Check leap year
print("Is 2015 a leap year?:", eth_date.is_leap_year)  # Output: True