#  File: Employee.py
#  Student Name: Austin Palmer
#  Student UT EID: ajp4344

class Employee:

    def __init__(self, **kwargs):
        """
        Employee information initialization
        """
        self._name = kwargs.get("name")
        self._id = kwargs.get("id")
        self._salary = kwargs.get("salary")
        
    @property
    def salary(self):
        """
        Employee salary getter
        """
        return (self._salary)

    @salary.setter
    def salary(self, salary):
        """
        Employee salary setter
        """
        self._salary = salary

    @property
    def name(self):
        """
        Employee name getter
        """
        return (self._name)

    @property
    def id(self):
        """
        Employee id getter
        """
        return(self._id)

    def __str__(self):
        """
        Returns employee information
        """
        output = "{} \n{} , {} , {}".format(
            self.__class__.__name__,
            self.name,
            self.id,
            self.salary
            )
        return(output)
        


############################################################
############################################################
############################################################
class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        """
        Initializes Permanent Employee information
        """
        Employee.__init__(self, **kwargs)
        self._benefits = kwargs.get('benefits')

    def cal_salary(self):
        """
        Returns weighted salary based on benefits
        """
        if (len(self._benefits) == 1):
            if(self._benefits[0] == 'health_insurance'):
                adj_salary = self.salary * 0.9
            
            elif(self.benefits[0] == 'retirement'):
                adj_salary = self.salary * 0.8
                

        elif (len(self._benefits) == 2):
            adj_salary = self.salary * 0.7
            
        return(float(adj_salary))


    @property
    def benefits(self):
        """
        Permanent employee benefits getter
        """
        return(self._benefits)

    @benefits.setter
    def benefits(self, benefits):
        """
        Permanent employee benefits setter
        """
        self._benefits = benefits

    def __str__(self):
        """
        Returns permanent employee information
        """
        output = "{}, {}".format(
            Employee.__str__(self),
            self.benefits
            )
        return(output)


############################################################
############################################################
############################################################
class Manager(Employee):
    def __init__(self, **kwargs):
        """
        manager info initialization
        """
        Employee.__init__(self, **kwargs)
        self._bonus = kwargs.get('bonus')

    def cal_salary(self):
        adj_salary = self.bonus + self.salary
        return(float(adj_salary))
        

    @property
    def bonus(self):
        """
        Bonus attr getter
        """
        return(self._bonus)

    def __str__(self):
        """
        Returns manager information
        """
        output = "{}, {}".format(
            Employee.__str__(self),
            self.bonus
            )
        return(output)


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        """
        Temp Employee info initialization
        """
        Employee.__init__(self, **kwargs)
        self.hours = kwargs.get('hours')

    def cal_salary(self):
        """
        Returns salary w/ respect to hours worked
        """
        adj_salary = self.hours * self.salary
        return(float(adj_salary))

    def __str__(self):
        """
        Returns Temp Employee Info
        """
        output = "{}, {}".format(
            Employee.__str__(self),
            self.hours
            )
        return(output)


############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        """
        Consultant info initialization
        """
        Temporary_Employee.__init__(self, **kwargs)
        self.travel = kwargs.get('travel')

    def cal_salary(self):
        """
        Returns salary w/ respect to hours worked and work trips
        """
        adj_salary = (self.hours * self.salary) + (self.travel * 1000)
        return(float(adj_salary))
        

    def __str__(self):
        """
        Returns Consultant Info
        """
        output = "{}, {}".format(
            Temporary_Employee.__str__(self),
            self.travel
            )
        return(output)


############################################################
############################################################
############################################################
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        """
        Consultant Manager info initialization
        """
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)
        
        # super().__init__(self, **kwargs)

    def cal_salary(self):
        """
        Returns salary w/ respect to hours worked, work trips, and bonus
        """
        adj_salary = (self.salary * self.hours) + (self.travel * 1000) + self.bonus
        return(float(adj_salary))

    def __str__(self):
        """
        Returns Consultant Manager Info
        """
        output = "{}, {}".format(
            Consultant.__str__(self),
            Manager.__str__(self)
            )
        return(output)


''' ##### DRIVER CODE #####
    ##### Do not change. '''


def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
