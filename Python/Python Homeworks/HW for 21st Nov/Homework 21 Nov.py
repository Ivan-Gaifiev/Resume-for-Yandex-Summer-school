class Programmer:
    """
    This class describes working programmer
    """
    # helpful dictionary for defining salary per hour according to the job title
    dict_salaries = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, job_title):
        """
        Function for initialisation of object of the class
        :param name: not empty string - name of the programmer
        :param job_title: string - Junior/Middle/Senior
        """
        # checking name for validity
        if name == '' or name.isdigit() is True:
            raise ValueError("The name must distinguish from empty string or number")
        self.__name = name
        # checking job_title for validity
        if job_title not in self.dict_salaries:
            raise ValueError("Title must be 'Junior' or 'Middle' or 'Senior'")
        self.__job_title = job_title
        self.__work_hours = 0  # number of hours programmer worked
        self.__salary_sum = 0  # sum of the salaries until salary()
        self.__salary_per_hour = self.dict_salaries[job_title]
        self.__history = []  # list for statistics/logging
        self.__set_stat('Hired')

    def __set_stat(self, description):
        """
        This function adds new state to the list for statistics
        :param description: string - description of the state
        """
        self.__history.append(f"<{self.__name}> <{self.__job_title}> <{description}>")

    @property
    def name(self):
        """
        This property (getter) allows user to get __name value
        :return: private attribute of the class
        """
        return self.__name

    def work(self, time):
        """
        This function adds time programmer worked
        :param time: positive integer
        """
        # checking time for validity
        if time <= 0:
            raise ValueError("Working time must be positive number")
        self.__work_hours += time
        # update sum of the salary according the time programmer worked
        self.__salary_sum += time * self.__salary_per_hour
        self.__set_stat(f'Worked for {time} hour(s) and earned {time * self.__salary_per_hour} tugrics')

    def bonus(self, amount):
        """
        This function adds bonus money to the sum of the salary
        :param amount: value of the bonus
        """
        # checking bonus for validity
        if amount <= 0:
            raise ValueError("Bonus must be positive number")
        self.__salary_sum += amount
        self.__set_stat(f'Got bonus: {amount} tugrics')

    def rise(self):
        """
        This function implements programmer promotion and updates salary per hour
        according to it.
        """
        match self.__job_title:
            case "Junior":
                self.__job_title = "Middle"
                self.__salary_per_hour = 15
            case "Middle":
                self.__job_title = "Senior"
                self.__salary_per_hour = 20
            case "Senior":
                self.__salary_per_hour += 1
        self.__set_stat(f'Promoted to {self.__job_title}')

    def info(self):
        """
        This function returns string in format: <name> <work_hours> <accumulated salary>
        :return: string
        """
        return f'<{self.__name}> <{self.__work_hours}>h. <{self.__salary_sum}>tgr.'

    def salary(self):
        """
        This function returns the value of the salary the programmer has to get
        :return: string
        """
        print(f'You have to give {self.__salary_sum} tgr. to the worker')
        self.__set_stat(f'Got the salary: {self.__salary_sum}')
        # nullify 2 parameters
        self.__salary_sum = 0
        self.__work_hours = 0

    def stat(self):
        """
        This function prints statistics with all steps of the programmer
        :return: lines of strings (1 line - 1 step)
        """
        print()
        print("All statistics here:")
        for i in self.__history:
            print(i)


# use-case
def main():
    programmer = Programmer("Marsik", 'Junior')
    programmer.work(750)
    print(programmer.info())
    programmer.rise()
    programmer.work(500)
    programmer.bonus(139)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.salary()
    programmer.stat()


main()
