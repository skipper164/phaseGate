"""""
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.problems = []


    def add_problem(self, problem):
        self.problems.append(problem)


p1 = Person ("justce", 20)
"""




class TimeWithProperties:
    def __init__(self, seconds =0, minutes=0, hours=0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self,value):
        if 0 > value > 59:
            raise ValueError("seconds must be between 0 and 59")
        self._seconds = value


    @property
    def minutes(self):
        return self._minutes


    @minutes.setter
    def minutes(self,value):
        if 0 > value > 59:
            raise ValueError("minutes must be between 0 and 59")
        self._minutes = value


    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self,value):
        if 0 > value > 23:
            raise ValueError("hours must be between 0 and 23")
        self._hours = value


    def set_time(self, seconds=0, minutes=0, hours=0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __str__(self):
        return f"{self.seconds}-{self.minutes}-{self.hours}"


