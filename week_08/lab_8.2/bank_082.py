class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0):
        self.name = '{} {}'.format(forename, surname)
        self.acc_number = BankAccount.next_account_number
        self.balance = int(balance)
        BankAccount.next_account_number += 1
        BankAccount.total_lodgements += 1

    def __str__(self):
        return ('Name: {}\nAccount number: {}\nBalance: {:.2f}'.format(self.name, self.acc_number, self.balance))

    def lodge(self, other):
        self.balance += other
        BankAccount.total_lodgements += 1

    def __iadd__(self, other):
        self.balance += other
        return self

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
