class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

# Example usage:
# account = Account("John Doe", 1000)
# account.deposit(500)
# account.withdraw(200)
