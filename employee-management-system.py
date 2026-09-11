class Person ():
  def __init__ (self,name,age):
   self.name =name
   self.age=age
  def display_info(self):
    print('Name=',self.name)
    print('Age=', self.age)
class Employee(Person):
  def __init__(self,name,age,employee_id,salary,department):
   super().__init__(name,age)
   self.employee_id=employee_id
   self.salary=salary
   self.department=department
  def display_info(self):
    super().display_info()
    print('Employee ID=',self.employee_id)
    print('Salary=',self.salary)
    print('Department=',self.department)
class DataAnalyst(Employee):
  def __init__(self,name,age,employee_id,salary,department,skills): 
    super().__init__(name,age,employee_id,salary,department)
    self.skills=skills
  def display_info(self):
    super().display_info()
    print('Skills=',self.skills)
  def performance_status(self):  
   if self.salary >= 100000 :
     print('Performance Level: Senior')
   elif self.salary >= 60000  : 
    print('Performance Level: Intermediate')
   else:
    print('Performance Level: Junior')
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Check Performance")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

     employee1 = DataAnalyst(
        input('Enter employee name: '),
        int(input('Enter employee age: ')),
        input('Enter employee ID: '),
        float(input('Enter employee salary: ')),
        input('Enter department: '),
        [
            input('Enter skill 1: '),
            input('Enter skill 2: '),
            input('Enter skill 3: ')
        ]
    )

     print("Employee added successfully!")   

    elif choice == "2":
        employee1.display_info()
    elif choice == "3":
        employee1.performance_status()

    elif choice == "4":
        print("Program closed")
        break

    else:
        print("Invalid choice")

