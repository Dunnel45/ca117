class BankAccount(object):
    next_account_number = 16555232
    account_type = 'General'

    def __init__(self, forename, surname, balance):
        self.name = '{} {}'.format(forename, surname)
        self.acc_number = BankAccount.next_account_number
        self.balance = int(balance)
        BankAccount.next_account_number += 1

    def lodge(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if self.balance < int(amount):
            print('Insufficient funds available')
        else:
            self.balance -= amount

    def __str__(self):
        l = []

        l.append('Name: {}'.format(self.name))
        l.append('Account number: {}'.format(self.acc_number))
        l.append('Account type: {}'.format(self.account_type))
        l.append('Balance: {:.2f}'.format(self.balance))
        return '\n'.join(l)

class CurrentAccount(BankAccount):
    float_overdraft = -1000
    account_type = 'Current'

    def withdraw(self, amount):
        if self.balance < int(amount) + CurrentAccount.float_overdraft:
            print('Insufficient funds available')
        else:
            self.balance -= int(amount)

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append('Overdraft: {:.2f}'.format(self.float_overdraft))
        return '\n'.join(l)

class SavingsAccount(BankAccount):
    ir = 0.01
    account_type = 'Savings'

    def apply_interest(self):
        self.balance *= (1 + SavingsAccount.ir)

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append('Interest rate: {}'.format(self.ir))
        return '\n'.join(l)
