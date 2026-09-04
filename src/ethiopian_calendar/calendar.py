from datetime import date as GregorianDate

class EthiopicDate:
    """Represents a date in the Ethiopian calendar."""
    
    AMHARIC_MONTHS = [
        "መስከረም", "ጥቅምት", "ህዳር", "ታህሳስ", "ጥር", "የካቲት", 
        "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሀምሌ", "ነሀሴ", "ጳጉሜ"
    ]
    
    LATIN_MONTHS = [
        "Meskerem", "Tikimt", "Hidar", "Tahsas", "Tir", "Yekatit",
        "Megabit", "Miyazya", "Ginbot", "Sene", "Hamle", "Nehase", "Pagume"
    ]

    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        self._validate()

    @property
    def is_leap_year(self) -> bool:
        return self.year % 4 == 3

    def _validate(self):
        if not (1 <= self.month <= 13):
            raise ValueError("Ethiopian month must be between 1 and 13.")
        
        max_days = 6 if (self.month == 13 and self.is_leap_year) else (5 if self.month == 13 else 30)
        
        if not (1 <= self.day <= max_days):
            raise ValueError(f"Invalid day {self.day} for month {self.month} in year {self.year}.")

    def month_name(self, lang: str = "latin") -> str:
        index = self.month - 1
        if lang.lower() == "amharic":
            return self.AMHARIC_MONTHS[index]
        return self.LATIN_MONTHS[index]

    def to_gregorian(self) -> GregorianDate:
        jdn = (1723856 + 365) + 365 * (self.year - 1) + (self.year // 4) + (30 * self.month) + self.day - 31
        f = jdn + 1401 + (((4 * jdn + 274277) // 146097) * 3) // 4 - 38
        e = 4 * f + 3
        g = (e % 1461) // 4
        h = 5 * g + 2
        day = (h % 153) // 5 + 1
        month = ((h // 153 + 2) % 12) + 1
        year = (e // 1461) - 4716 + (12 + 2 - month) // 12
        return GregorianDate(year, month, day)

    @classmethod
    def from_gregorian(cls, g_date: GregorianDate) -> "EthiopicDate":
        a = (14 - g_date.month) // 12
        y = g_date.year + 4800 - a
        m = g_date.month + 12 * a - 3
        jdn = g_date.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
        r = (jdn - 1723856) % 1461
        n = (r % 365) + 365 * (r // 1640)
        year = 4 * ((jdn - 1723856) // 1461) + (r // 365) - (r // 1460)
        month = (n // 30) + 1
        day = (n % 30) + 1
        return cls(year, month, day)

    def __repr__(self) -> str:
        return f"EthiopicDate(year={self.year}, month={self.month}, day={self.day})"

    def __str__(self) -> str:
        return f"{self.day} {self.month_name('latin')} {self.year}"