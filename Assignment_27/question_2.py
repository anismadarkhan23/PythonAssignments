class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.account_holder_name = name
        self.account_balance = amount
    
    def display_account_details(self):
        print(f"Account holder name: {self.account_holder_name}")
        print(f"Saving account balance is: {self.account_balance}")

    def deposit_amount(self):
        depAmount = int(input("Enter the amount to be deposited: ₹")) 
        self.account_balance += depAmount

    def withdraw_amount(self):
        withAmount = int(input("Enter the amount to be withdrawn: ₹")) 
        if withAmount > self.account_balance:
            print("Insufficient Balance in account")
        else:
            self.account_balance -= withAmount
        
    def calculate_interest(self):
        interest = (self.account_balance * BankAccount.ROI) / 100
        print(f"Total interest earned on account balance is {interest}")
        self.account_balance += interest
        print(f"Total saving account balance after interest earned is ₹{self.account_balance}")

print("-------------------------- Bank Details ------------------------------")
ba_obj1 = BankAccount("Anis Madarkhan", 100000)
print("-" * 70)
ba_obj1.display_account_details()
print("-" * 70)
ba_obj1.deposit_amount()
ba_obj1.display_account_details()
print("-" * 70)
ba_obj1.calculate_interest()
print("-" * 70)
ba_obj1.withdraw_amount()
ba_obj1.display_account_details()
print("-" * 70)
ba_obj1.calculate_interest()
print("-" * 70)
ba_obj1.display_account_details()
print("-" * 70)
print("-------------------------- Bank Details ------------------------------")