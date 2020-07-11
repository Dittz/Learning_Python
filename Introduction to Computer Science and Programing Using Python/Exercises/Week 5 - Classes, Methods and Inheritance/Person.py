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


be = Person('Bernardo Dittz')
be.setBirthday(1, 28, 1988)
be.getLastName()
be.getAge()

pati = Person('Patricia Winter')
pati.setBirthday(9,27,1992)

personList = [pati, be]
for e in personList:
    print(e)
print('------------------')
personList.sort()
for e in personList:
    print(e)
