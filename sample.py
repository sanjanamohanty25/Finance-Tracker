import calendar as cal
from datetime import date

today = date.today()
month_year = cal.monthrange(today.year, today.month)
per_day = round(3000 /month_year[1],2)
print(per_day)

import day_wise as dw
dw.day_wise(3000)


