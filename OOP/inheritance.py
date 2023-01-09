class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print('i am from Rectangle')
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        print('i am from Square')
        return self.length + self.width


class Test(Square):
    def __init__(self, trying):
        super().__init__(trying)

    def area(self):
        print('i am from Test')
        return self.length / self.width

class my_name():
    def __init__(self):
        print('my Name is Savvas')

class Cube(Test,my_name):

    def __init__(self, value):
        super(my_name,self).__init__()
        super(Test, self).__init__(value)


    def surface_area(self):

        face_area = super(Square,self).area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def area(self):
        return self.length + self.width




"""https://realpython.com/inheritance-composition-python/#whats-composition"""

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

class Employee:
    def __init__(self, id: int, name: str) -> object:
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self,id,name,weekly_salary):
        super().__init__(id,name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self,id,name,hours_worked,hour_rate):
        super().__init__(id,name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission



class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')
        
class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')