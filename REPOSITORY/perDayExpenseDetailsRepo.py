from REPOSITORY.app import *

def insert(itemName, Amount):
    # query = """ INSERT INTO perDayExpenseDetails(itemName, Amount) 
    # values (itemName, Amount); """
    query = "INSERT INTO perDayExpenseDetails (itemName, Amount) VALUES (%s, %s)"
    cursor.execute(query, (itemName, Amount))
    conn.commit()


