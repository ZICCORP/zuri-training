
class Budget:

    def __init__(self,**categories):
        self.categories = categories
        print(self.categories)

    def deposit(self,amount,category):
        self.categories[category] = self.categories[category] + amount
        print('You deposited the sum of $'+str(amount)+' '+ 'to '+category)
    
    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print("Insufficient Balance")
        else:

            self.categories[category] = self.categories[category] - amount
            print('You withdrew the sum of $'+str(amount)+' from '+ category)

    def transfer(self,amount,debitCategory,creditCategory):
        if amount > self.categories[debitCategory]:
            print('Insufficient Balance')
        else:
            self.categories[debitCategory] = self.categories[debitCategory] - amount
            self.categories[creditCategory] =  self.categories[creditCategory] + amount
            print('You transfered the sum of $'+ str(amount) + ' ' + 'from ' + debitCategory + ' to '+ creditCategory )
    
    def checkBalance(self,category):
        print('Your '+ category + ' budget balance is ' + str(self.categories[category]))
        

mybudget= Budget(food=100, clothing=200, rent=3000,entertainment=150)
mybudget.deposit(150,'food')
mybudget.withdraw(50,'rent')
mybudget.transfer(70,'entertainment','clothing')
mybudget.checkBalance('clothing')

