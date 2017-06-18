import self as self

from com.satishsoft.AbstractDemo import Employee


class EmployeeOne(Employee):
    #@abstractmethod

        def cal_sal(self, sal):
            finalsalary = sal * 1.10
            return finalsalary

emp11 = EmployeeOne()
print("wow")
print(emp11.cal_sal(20800))