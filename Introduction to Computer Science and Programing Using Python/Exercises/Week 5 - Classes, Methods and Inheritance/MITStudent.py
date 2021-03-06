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



p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person ('Steve Wozniak')
    
personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)
    
print('---------------')

personList.sort()

for e in personList:
    print(e)
print('---------------')


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
        return (self.getLastName() + ' says: ' + utterance)

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)   


personList = [m1, m2, m3]
for e in personList:
    print('Id Number: {} - {}'.format(e.getIdNum(), e))
print('---------------')
personList.sort()
for e in personList:
    print('Id Number: {} - {}'.format(e.getIdNum(), e))
print('---------------')




p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

p1 < p2


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


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo de Caprio')

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))


