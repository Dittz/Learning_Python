import datetime

class Person(object):
    def __init__(self, name):
        '''Create a person called name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        '''Set's person birthday to a date'''
        self.birthday = datetime.date(year, month, day)

    def __lt__(self, other): #lt stands for less than
        '''Returns True if self's name is lexicographically less
        than others name and false otherwise'''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def getAge(self):
        '''returns person current age in days'''
        if self.birthday == None:
            raise ValueError
        return(datetime.date.today() - self.birthday).days

    def __str__(self):
        '''prints the string name'''
        return self.name



class MITPerson(Person):
    nextIdNum = 0 # class variable that increases with news instances

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum # sets the id number for self
        MITPerson.nextIdNum += 1 # alter the id number so the next instance of MITPerson doesn't have the same id number

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.name + ' says: ' + utterance)



class Student(MITPerson):
    pass



class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, 'Dude, ' + utterance)



class Grad(Student):
    pass



class TransferStudent(Student):
    pass



def isStudent(obj):
    return isinstance(obj, Student)



class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course {} we say '.format(self.department)
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that {}'.format(topic))




class Grades(object):
    '''A mapping from students to a list of grades'''
    def __init__(self):
        '''Creates an empty grade book'''
        self.students = [] #list students objects
        self.grades = {} # maps idNum -> list of grades
        self.isSorted = True #True is self.students is sorted

    def addStudent(self, student):
        '''Assumes student is type Student
           Add student to the grade book'''
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        '''Assumes: grade is a float
           Add grade to the list of grades for student'''
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
        
    def getGrades(self, student):
        '''Return a list of grades for student'''
        try:     #return a copy of student's grades 
            return self.grades[student.getIdNum()][:] #return a copy so the original is not altered
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        '''Return a list of the students in the gradebook'''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        #return a copy of list of students



def gradeReport(course):
    '''Assumes: course is of type grades'''
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades.')
    return '\n'.join(report)

    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

            
#Creating data base of students:
ug1 = UG('Matt Damon', 2017)
ug2 = UG('Ben Affleck', 2017)
ug3 = UG('Lin Manuel Miranda', 2018)
ug4 = Grad('Mark Zuckerberg')
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

#Creating a grade book:
six00 = Grades()

#adding the students into the grade book:
#the order that I've choosed to add the students doesn't matter cause I will order them by id number
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug3)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)

#adding grades to the students
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print()

#printing the report:
print(gradeReport(six00))

#updating grades:
six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print()

#printing the report:
print(gradeReport(six00))

print()

for s in six00.allStudents():
	print(s)








        
