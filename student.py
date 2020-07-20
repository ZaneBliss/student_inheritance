from nss_person import NSSPerson

class Student(NSSPerson):

    def __init__(self, fname, lname, slack, cohort):
        super().__init__(fname, lname, slack, cohort)
        self.exercises = list()