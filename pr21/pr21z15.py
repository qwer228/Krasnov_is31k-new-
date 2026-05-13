class BankAccount:
    __slots__ = ('balance',)
    
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" Внесено: {amount}, баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(" Недостаточно средств")
        else:
            self.balance -= amount
            print(f" Снято: {amount}, баланс: {self.balance}")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)  # Проверка
