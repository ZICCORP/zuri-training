from datetime import datetime
import random

today = datetime.now()
# Database that stores user's account details  
database ={5169137116:['Frank', 'Chuka','contact@frankchuka.com','testpass123',2000]}

# get a list containing all the account numbers in the database
accountNumbers= list(database.keys())

# A dictionary that map month numbers to name of the month e.g march maps to the number 3
calendar = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}


# check if time is in Am or Pm
if today.hour >= 12:
    am_pm = 'PM'
else:
    am_pm = 'AM'

def init():
    print('ZURIBANK PLC')

    haveAccount = int(input("Do you have an account with us: 1 (yes) 2(no) \n"))

    if (haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected an invalid option")
        init()
    
def login():
    print("******** Login ******")
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

                     
    print('Invalid account or password')
    login()
    
    
def logout():
    login()

def register():
    print('***** Register *****')
    email = input("What is your email address?\n")
    first_name =input("What is your first name?\n")
    last_name =input("What is your last name?\n")
    password =input("create a password for yourself\n")
    accountBalance = 0

    accountNumber = generateAccountNumber()
    
    database[accountNumber] = [first_name, last_name,email,password,accountBalance]

    print("Your Account has been created")
    print("Your Account number is " + str(accountNumber))
 
    login()

def bankOperation(user):
      # display the date in the format 'day month-name year' i.e 3 march 2021
      print('Date: '+str(today.day)+' '+calendar[str(today.month)]+' '+ str(today.year))

      # display the time by appending am or pm 
      print('Time: '+str(today.hour)+':'+str(today.minute)+' '+am_pm+'\n')
      print("Welcome %s %s" %(user[0],user[1]))
      selectedOption = int(input("What would you like to do? 1. Cash Deposit  2. Withdrawal  3.Complaint  4.Logout 5.exit \n"))
      if(selectedOption == 1):
        depositOperation(user) 

      elif(selectedOption == 2):
        withdrawalOperation(user)
      elif(selectedOption ==3):
        complaint()                      
      elif(selectedOption ==4):
        logout()
      elif(selectedOption ==5):
        exit()
      else:
        print("Invalid option selected")
      bankOperation(user)
      
                     
                      
def withdrawalOperation(user):
    amount= input('How much would you like to withdraw? \n')
    accountBalance = user[4]
    if int(amount) > accountBalance:
        print('Insufficient Balance\n')
    else:
        print("take your cash\n")

    

def depositOperation(user):
    print("Deposit Operation")
    amount = input('How much would you like to deposit? \n')
    accountBalance = user[4]
    print('Current Balance: '+ str(accountBalance + int(amount)) + ' zuri_naira')


def complaint():
    input('What issue will you like to report? \n')
    print("Thank you for contacting us \n") 
      


def generateAccountNumber():

    print("Generating Account Number")

    # making sure a unique account number is generated
    while True:
        account_number = random.randrange(1111111111,9999999999)
        if account_number not in accountNumbers:
           return account_number


init()
     





