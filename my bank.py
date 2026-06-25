class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}, ваш новый баланс: {self.balance}\n")
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError(f"{self.owner}, у вас недостаточно денег на счету!")
        else:
            self.balance -= amount
            print(f"Деньги успешно списаны!\nВаш баланс: {self.balance}\n")
            
    def transfer(self, other, amount):
        if self.balance < amount:
            raise ValueError(f"{self.owner}, у вас недостаточно денег на счету!")
        else:
            self.balance -= amount
            other.balance += amount
            print(f"Деньги успешно переведены {other.owner}!\nВаш баланс: {self.balance}\n")
            
    def __str__(self):
        return f"Счёт {self.owner}: {self.balance} ₽"
ac = BankAccount("Степан", 100)
ab = BankAccount("Кирилл", 200)
ac.deposit(10)
ac.withdraw(20)
ac.transfer(ab, 30)
print(ac)