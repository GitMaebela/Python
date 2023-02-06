from norea_bank_account import BankAccount

# creating a sample account
sample_account = BankAccount("Milwaukee Maebela", 65000)

# making some transactions
sample_account.deposit(1000)
sample_account.withdraw(500)
sample_account.withdraw(1500)
sample_account.withdraw(4560)
sample_account.withdraw(7612)
sample_account.deposit(2000)

# viewing transaction history for the past 3 months
sample_account.view_transaction_history(3)