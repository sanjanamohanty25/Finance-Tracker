import calendar as cal
from datetime import date

def calculatePerDayExpenditure(monthlyBudget):
    '''
        monthlyBudget -> Budget for this month
        Returns per day allowance
    '''
    today = date.today()
    daysOfMonth = cal.monthrange(today.year, today.month)
    perDayExpenditure = round(monthlyBudget/ daysOfMonth[1],2)
    return perDayExpenditure



# budget = int(input("Enter your monthly budget: "))
# per_day1 = day_wise(budget)
# print(f"Your budget for per day this month is {per_day1}")
