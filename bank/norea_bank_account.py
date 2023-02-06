import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append({'transaction_type': 'deposit', 'amount': amount, 'date': datetime.datetime.now()})
        print(f"Deposited {amount} to {self.name}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append({'transaction_type': 'withdraw', 'amount': amount, 'date': datetime.datetime.now()})
            print(f"Withdrew {amount} from {self.name}'s account. New balance: {self.balance}")
        else:
            print(f"Insufficient balance in {self.name}'s account. Current balance: {self.balance}")

    def check_balance(self):
        print(f"{self.name}'s current balance: {self.balance}")

    def view_transaction_history(self, period_in_months):
        period_in_seconds = period_in_months * 30 * 24 * 60 * 60
        current_time = datetime.datetime.now
