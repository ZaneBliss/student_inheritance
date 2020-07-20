from nss_person import NSSPerson

class Instructor(NSSPerson):
    
    def __init__(self, fname, lname, slack, cohort, specialty):
        super().__init__(fname, lname, slack, cohort)
        self.specialty = specialty

    def assignExercise(self, student, exercise):
        student.exercises.append(exercise)
    