from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

chicken_monkey = Exercise('Chicken Monkey', 'Swift')
add_three = Exercise('Add Three', 'Python') 
guess_num = Exercise('Guess Number', 'Python')
coins_rupees = Exercise('Coins to Rupees', 'Javascript')

exercises = list()
exercises.extend([chicken_monkey, add_three, guess_num, coins_rupees])

cohort1 = Cohort('Evening Cohort 1')
cohort2 = Cohort('Evening Cohort 2')
cohort3 = Cohort('Day Cohort 1')

kaleb = Student('Kaleb', '?', 'iamkaleb', 40)
zach = Student('Zach', '?', 'iamzack', 40)
sophia = Student('Sophia', 'Lamb', 'iamsophia', 40)
sam = Student('Sam', 'Breckers', 'iamsam', 40)

students = list()
students.extend([kaleb, zach, sophia, sam])


joe = Instructor('Joe', 'Shepherd', 'joeshep', 40, 'Dad jokes')
bryan = Instructor('Bryan', 'Nilsen', 'bnilsen', 40, 'Bad jokes')
sage = Instructor('Sage', 'Klein', 'mesage', 40, 'Figma')

joe.assignExercise(kaleb, chicken_monkey)
bryan.assignExercise(zach, add_three)
sage.assignExercise(sophia, guess_num)
joe.assignExercise(sam, coins_rupees)