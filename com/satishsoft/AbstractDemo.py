from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def cal_sal(self,sal):
        pass
"""class Developer(Employee):
     def cal_sal(self,sal):
         finalsalary = sal * 1.10
         return finalsalary
emp1=Developer()
print(emp1.cal_sal(2000))"""

"""class a(Employee):
    print("vadab")

    def cal_sal(self, sal):
        finalsalary = sal * 2.10
        return finalsalary

emp2=a()
print(emp2.cal_sal(2000))"""

# other class





