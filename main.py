from budget_category import BudgetCategory #import the BudgetCategory class from the budget_category module

def main(): #main function wrapper for example code
    food_category = BudgetCategory("Food", 500) #example code
    food_category.add_expense(100) #example code
    food_category.display_category_summary() #example code
    

if __name__ == "__main__": #check the current module is not being imported
    main() #run the main function