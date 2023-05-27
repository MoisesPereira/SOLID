class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient balance for withdrawal.')
        self.balance -= amount
        print(f"Value - self.balance: {self.balance}")
