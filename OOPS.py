# It is a way to program practically
'''
"Everything in python is an Object "
Object can be of any Class (i.e Monitor is an object and Classes can be Dell, Asus, LG)
Object is an instance of class
ex:
Car-> Tesla // Tesla = Car()
'''
'''
Class: Data type is class and variable of particular data type is an object
Class is a blueprint of how an object behaves.
Class={Data,Functions}
#Basic structure of a class
class Name of class(Should be in CamelCase):
    color="blue" #data
    model="sports" #data
    def calc_speed(km,time):
        #some code
'''
class Atm:
    #Function vs Method
    '''Methods: Functions defined in a particular Class Expressed as Object_of_Class.Method()'''

    def __init__(self): #Constructor : It's a method which automatically execute code inside it of the working class. 
        self.pin = ""  #these are objects/variables of class Atm
        self.balance = 0
    

        self.menu()

    def menu(self):
        user_input = input(''' 
                   WELCOME 
        First you have to enter your PIN
                1:Enter 1 Set PIN:
                    
        Then only you can perform any Transactions
                
        ''')
        if user_input == '1':
            self.Create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.Check_balance()
        else :
            print("Exit")
            
    def Create_pin(self):
        self.pin = input("Enter your PIN:")
        print("PIN has been SET successfully")
    
    def deposit(self):
        temp = input("Enter your PIN:")
        if temp == self.pin:
            amount = int(input("Enter the amount:"))
            self.balance=self.balance + amount
            print("Deposit succesful")
        else:
            print("Invalid PIN")
    def withdraw(self):
        temp = input("Enter your PIN:")
        if temp == self.pin:
            amount = int(input("Enter the amount:"))
            if amount<self.balance:
                self.balance = self.balance - amount
                print("Withdrawal Successfully")
            else:
                print("NO Enough Balance")
    def Check_balance(self):
        temp = input("Enter your PIN:")
        if temp == self.pin:
            print("Your Current Balance:",self.balance)
        else:
            print("Invalid PIN")
                           
        
