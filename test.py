import day_wise as dw
import expenditure as ep
from tabulate import tabulate


def runTestCode():
    '''
    This function is a test module that combines all the modules
    '''
    while True:
        '''
            Handles edge cases for the input 'monthlyBudget'
        '''
        try: 
            monthlyBudget = int(input("Enter your monthly budget: "))
            if monthlyBudget < 0:
                print("Your monthly budget can not be negative. Please enter a valid number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    
    #perDayAllowance = dw.calculatePerDayExpenditure(monthlyBudget)
    print(f"Your per day allowance is {dw.calculatePerDayExpenditure(monthlyBudget)}")

    itemAmountMap = ep.checkExpenditure()
    print(tabulate(itemAmountMap.items(), headers= ["Item Name", "Amount"], tablefmt="grid"))

    totalExpenditureToday = sum(itemAmountMap.values())
    print(f"Your total expenditure for the day is {totalExpenditureToday}")

    
runTestCode()