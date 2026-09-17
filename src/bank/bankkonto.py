class BankKonto:
    def __init__(self, logger):
        self.balance = 0
        self.logger = logger

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount and amount > 0:
            text = f"withdraw: kunde inte ta ut {amount} från kontot"
            self.logger.log(text)
            return False

        else:
            self.balance -= amount
            text = f"withdraw: {amount} kr, saldo {self.balance} kr"
            self.logger.log(text)
            return True

    def interest(self):
        if self.balance > 0:
            self.balance *= 1.05


class Logger:
    def __init__(self):
        self.text = ""

    def log(self, info):
        self.text = info


class Transaction:
    def transfer(self, amount, from_account, to_account):
        if from_account.withdraw(amount):
            to_account.deposit(amount)
