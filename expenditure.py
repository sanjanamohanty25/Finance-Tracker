itemAmountMap = {}

def addItemsToExpenditure(itemsToBeAdded):
    '''
        itemsToBeAdded -> flag variable, by defalut set to true
        This function adds all the items and its amount to a dictionary/hashmap
    '''

    while itemsToBeAdded:
        try:
            amountSpentToday = float(input("Enter amount spent: "))
        except ValueError:
            print("Invalid amount. Please enter amount in number")
            return
        
        itemName = input("Enter the item spent on: ").strip()
      
        itemAmountMap[itemName] = amountSpentToday
        moreItem = input("Do you want to add more expenses? Y/N \n").strip().lower()
        
        if moreItem == "y":
            continue
        elif moreItem != 'n' and moreItem != 'y':
            moreItem = input("Please input either 'Y' or 'N' \n")
            continue
        else:
            itemsToBeAdded = False



def checkExpenditure():
    '''
        This function checks if user has any expenses to add for the day
        Returns -> resulting dictionary
    '''

    expend = input("Do you want to add expenses? Y/N \n").strip().lower()
    itemsToBeAdded = True
    if expend == "y":
        addItemsToExpenditure(itemsToBeAdded)
 
    elif expend == "n":
        print("No expenses to calculate for today.")

    else: 
        expend = input("Please input either 'Y' or 'N' \n ").strip().lower()
        addItemsToExpenditure(itemsToBeAdded)



    return itemAmountMap


