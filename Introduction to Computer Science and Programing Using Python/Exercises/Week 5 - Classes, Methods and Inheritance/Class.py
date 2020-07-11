class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=''):
        self.name = newname

    def __str__(self):
        return 'Animal: {} \nAge: {}'.format(self.name, self.age)
        


class Cat(Animal):
    def speak(self):
        print('meow')

    def __str__(self):
        return 'Cat: {} \nAge: {}'.format(self.name, self.age)



class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag #rid = registration id
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2
        
    def speak(self):
        print('meep')

    def __str__(self):
        return 'Rabbit: {} \nAge: {} \nTag: {}'.format(self.name, self.age, self.rid)

    def __add__(self, other):
        #add a new rabbit
        return Rabbit(0, self, other) #age= 0, 1st parent in self, second parent is other

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

#example:

r1 = Rabbit(3)
r1.set_name('r1')
r2 = Rabbit(4)
r2.set_name('r2')

r4 = r1+r2
r4.set_name('r4')

print(r4)
print('')
print(f'r4 parent1:\n{r4.get_parent1()}')



class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return str(self.friends)

    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print('hello')

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.get_age() > other.get_age():
            print('{} is {} years older than {}'.format(self.get_name(), diff, other.get_name()))
        else:
            print('{} is {} years older than {}'.format(other.get_name(), -diff, self.get_name()))



class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self,major):
        self.major = major

    def __str__(self):
        return 'Student: {} \nAge: {} \nMajor: {}'.format(self.name, self.age, self.major)

a = Person('Rubens', 75)
b = Person('Edgar', 90)


                
