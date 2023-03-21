class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        print(f"Name: {self.name},\nAge: {self.age}")
        
class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary
    
    def get_details(self):
        super().get_details()
        print(f"ID: {self.id},\nSalary: {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, age, id, salary, department):
        super().__init__(name, age, id, salary)
        self.department = department
    
    def get_details(self):
        super().get_details()
        print(f"Department: {self.department}")
    
MGR = Manager("Rifki yandi", 12, 210511156,"Programmer","Technical")
MGR.get_details() 