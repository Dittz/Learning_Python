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


def MITPerson(Person):
    nextIdNum = 0 # class variable that increases with news instances

    def __init__(self, name):
        Person.__init__(self, name)
        self.IdNum = MITPerson.nextIdNum #sets the id number for self
        MITPerson.nextIdNum += 1 #alter the id number so the next instance of MITPerson doesn't have the same id number

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + ' says:' + utterance)


p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person ('Steve Wozniak')
    
