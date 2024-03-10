# Create a class representing a simple bank account with deposit and withdraw methods

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposited: {amount}")
        self.get_balance()

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            self.get_balance()
        else:
            print("Insufficient funds")
        

new_account = BankAccount(float(input("Enter bank account balance: ")))
new_account.deposit()
new_account.withdraw()