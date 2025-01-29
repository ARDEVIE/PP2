class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def checkBal(self):
        print(f"\n{self.balance} Tenge\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} on deposit\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money\n")
        else:
            self.balance -= amount
            print(f"{amount} tenge taken from deposit\n")


onlineBank = True
name_of_deposit = Account(input('write the name\n'))
while onlineBank:
    a = (input("take - 1. \nput - 2. \ncheck - 3.\nturn off - 4.\n"))
    if a == '1':
        try:
            name_of_deposit.withdraw(int(input('\nHow much?\n')))
        except:
            print("\nError\n")
            pass
    if a == '2':
        try:
            name_of_deposit.deposit(int(input('\nHow much?\n')))
        except:
            print("\nError\n")
            pass
    if a == '3':
        name_of_deposit.checkBal()
    if a == '4':
        onlineBank = False
    if a not in ['1', '2', '3', '4']:
        print('\nChoose\n')
        continue