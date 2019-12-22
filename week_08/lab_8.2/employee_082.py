class Employee(object):
    next_employee_number = 0

    def __init__(self, name, hours_worked=0, hourly_rate=9.25):
        self.name = name
        self.id = Employee.next_employee_number
        self.hours = hours_worked
        self.rate = hourly_rate

        Employee.next_employee_number += 1

    def __str__(self):
        return ('Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}'. format(self.name, self.id, self.hours, self.rate, (self.hours * self.rate)))

    def add_hours(self, other):
        self.hours = self.hours + other
        return self.hours
