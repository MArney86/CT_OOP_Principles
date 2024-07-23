#Task 1
class BudgetCategory:
    def __init__(self, category, budget):
        self.__category = category #category of the budget
        self.__budget = budget #allocated budget for the category
        self.__expenses = 0 #expenses for task 3

#Task 2
    def get_category(self): #method to return the object's category
        return self.__category  #return the object's category
    
    def set_category(self, category): #method to set/update the object's category
        self.__category = category #set/update the object's category

    def get_allocated_budget(self): #method to return the object's allocated budget
        return self.__budget #return the object's allocated budget

    def set_allocated_budget(self, budget): #function to set/update the object's allocated budget
        if budget > 0: #verify that the given budget is a positive number
            self.__budget = budget #set/update the budget to the given value
        else: #give budget it negative
            print("Budget must be a positive number.") #notify user that the value is negative

#Task 3
    def add_expense(self, amount): #method to add an expense
        if amount > 0: #verify that the expense amount is a positive number
            self.__expenses += amount #add the expense to __expenses
        else: #expense is not positive
            print("Expense amount must be a positive number") #notify the user that the give expense is negative

#Task 4
    def display_category_summary(self): #method to print the current state of the budget
        remaining_budget = self.__budget - self.__expenses #calculate the remaining budget
        print(f"\nBudget Category: {self.__category}") #print the category
        print(f"Category Allocated Budget: {self.__budget}") #print the allocated budget
        print(f"Category Expenses: {self.__expenses}") #print the tracked expenses
        print(f"Category Remaining Budget: {remaining_budget}") #print the remaining budget