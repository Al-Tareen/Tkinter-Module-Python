class Employee():
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_Employee(self):
        print("Employee: " + self.name)
        print(self.name + ": " + "Phone Number: " + self.phone)

class ProductionWorker(Employee):
    
    def __init__(self, name, phone, shift, hourly_pay):
        super().__init__(name, phone) #<-- Passes (name, phone) parameters to parent (Employee) class.
        
        self.shift = shift
        self.hourly_pay = hourly_pay

    def get_ProductionWorker(self):
        
        self.get_Employee() #<-- Call getter function from Employee class with self inheritance.
        
        if self.shift == 1:
            print(self.name + ": " + "Shift: " + "Day-Shift")
        else:
            print(self.name + ": " + "Shift: " + "Night-Shift")

        print(self.name + ": " + "Hourly Pay-Rate: $" + str(self.hourly_pay))

emp1 = ProductionWorker(input("Please enter the Name of your Employee: "), str(input("Please enter the Phone Number for your Employee: ")),int(input("Please enter the Shift for your Employee. \nType 1 for Day Shift or 2 for Night Shift: ")), float(input("Please enter the Hourly Pay Rate for your Employee: ")))

print()
print("Employee successfully entered into database.")
print("Thank you for using AlTech Financial Solutions.")
print()

emp1.get_ProductionWorker()
