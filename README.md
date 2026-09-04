# Ethiopian Calendar (`ethiopian-calendar`)

A lightweight, standards-compliant Python library for converting between the Ethiopian calendar (Ge'ez calendar) and the Gregorian calendar system.

## Features

- **Bidirectional Conversion:** Seamless conversion between `EthiopicDate` and standard Python `datetime.date`.
- **Leap Year Handling:** Accurate calculation of 4-year leap cycles, including 6-day *Pagume* months.
- **Multilingual Support:** Access month names in both Amharic script (e.g., መስከረም) and Latin transliteration (e.g., Meskerem).
- **Zero External Dependencies:** Built entirely with Python standard library components.
- **Modern Packaging:** Structured using the recommended `src/` layout with unit test coverage.

## Installation

Clone the repository and install in editable mode:

```bash
git clone [https://github.com/YOUR_USERNAME/ethiopian-calendar.git](https://github.com/YOUR_USERNAME/ethiopian-calendar.git)
cd ethiopian-calendar
pip install -e .

## Quick Start

```python
from datetime import date
from ethiopian_calendar import EthiopicDate

# Create an Ethiopian date
eth_date = EthiopicDate(year=2015, month=1, day=1)
print(eth_date)  # Output: 1 Meskerem 2015
print(eth_date.month_name(lang="amharic"))  # Output: መስከረም

# Convert Ethiopian date to Gregorian date
greg_date = eth_date.to_gregorian()
print(greg_date)  # Output: 2022-09-11

# Convert Gregorian date to Ethiopian date
converted_eth = EthiopicDate.from_gregorian(date(2022, 9, 11))
print(converted_eth)  # Output: 1 Meskerem 2015

# Check if a year is a leap year
print(eth_date.is_leap_year)  # Output: True
```