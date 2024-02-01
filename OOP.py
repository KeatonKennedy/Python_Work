# OOP Work
        
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info_person(self):
        print(self.name, self.age)
        
class Employee(Person):
    def __init__(self):
        super().__init__(name,age)
        def __init__(self,position):
            self.position = position
            
        def display_info_employee(self):
            print(self,position, self.name, self.age)


person = Person('Victor','19')
person.display_info_person()
employee = Person('Manager','Victor','19')
employee.display_info_employee()



