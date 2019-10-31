from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def showEmployeeDetails(self):
        pass

    def addEmployee(self, employee):
        return None

    def removeEmployee(self, employee):
        return None


class Developer(Employee):
    def __init__(self, empId, name, position):
        self._empId = empId
        self._name = name
        self._position = position

    def showEmployeeDetails(self):
        print("{} {}".format(self._empId, self._name))


class Manager(Employee):
    def __init__(self, empId, name, position):
        self._empId = empId
        self._name = name
        self._position = position

    def showEmployeeDetails(self):
        print("{} {}".format(self._empId, self._name))


class CompanyDirectory(Employee):
    def __init__(self):
        self._employeeList = []

    def addEmployee(self, employee):
        self._employeeList.append(employee)

    def removeEmployee(self, employee):
        self._employeeList.remove(employee)

    def showEmployeeDetails(self):
        for employee in self._employeeList:
            employee.showEmployeeDetails()


dev1 = Developer("D101", "John Paul", "Python Developer")
dev2 = Developer("D102", "Ryan Harris", "Java Developer")

Engineers_directory = CompanyDirectory()
Engineers_directory.addEmployee(dev1)
Engineers_directory.addEmployee(dev2)

man1 = Manager("M101", "Mark Johnson", "Accounts Manager")
man2 = Manager("M102", "John Markson", "Hiring Manager")

Managers_directory = CompanyDirectory()
Managers_directory.addEmployee(man1)
Managers_directory.addEmployee(man2)

directory = CompanyDirectory()
directory.addEmployee(Engineers_directory)
directory.addEmployee(Managers_directory)
directory.showEmployeeDetails()

a = "21"
dev1.addEmployee(a)





