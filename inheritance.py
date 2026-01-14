# # Create a BankAccount system where SavingsAccount and CheckingAccount both inherit from Account, and PremiumAccount uses multiple inheritance to combine both for premium banking features.
# This demonstrates combining financial behaviors like deposits, withdrawals, and interest calculation.�Problem StatementBase Account handles balance and transactions. 
# SavingsAccount adds interest earning, CheckingAccount adds overdraft protection.
#  PremiumAccount inherits from both to support interest on positive balances while allowing overdrafts, with a combined monthly statement generator.�


class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

# SavingsAccount inherits from Account
class SavingsAccount(Account):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")

# CheckingAccount inherits from Account
class CheckingAccount(Account):
    def __init__(self, name, balance=0, overdraft_limit=500):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
        else:
            print("Overdraft limit exceeded")

# PremiumAccount uses multiple inheritance
class PremiumAccount(SavingsAccount, CheckingAccount):
    def __init__(self, name, balance=0, interest_rate=0.05, overdraft_limit=1000):
        SavingsAccount.__init__(self, name, balance, interest_rate)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        if self.balance > 0:
            super().calculate_interest()

    def generate_monthly_statement(self):
        print("\n--- Monthly Statement ---")
        print("Account Holder:", self.name)
        for t in self.transactions:
            print(t)
        print("Final Balance:", self.balance)


# --------- TESTING / PRINTING EVERYTHING ---------

# Create a Savings Account
sa = SavingsAccount("Adarsh", 1000)
sa.deposit(500)
sa.withdraw(200)
sa.calculate_interest()

print("\nSavings Account Balance:", sa.get_balance())
print("Savings Account Transactions:")
for t in sa.transactions:
    print(t)


# Create a Checking Account
ca = CheckingAccount("Rahul", 500)
ca.withdraw(800)   # overdraft allowed
ca.deposit(300)

print("\nChecking Account Balance:", ca.get_balance())
print("Checking Account Transactions:")
for t in ca.transactions:
    print(t)


# Create a Premium Account
pa = PremiumAccount("Soni", 2000)
pa.deposit(1000)
pa.withdraw(2500)  # overdraft allowed
pa.calculate_interest()
pa.generate_monthly_statement()

