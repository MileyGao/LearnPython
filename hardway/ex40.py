class Person(object):
    def __init__(self,name):
        print "create a new Person"
        self.name = name
        self.height = 175
        #return self
    def speak(self):
        print "my name is:", self.name

miley = Person("Miley")
miley.height = 190 
miley.speak()
kingo = Person("Kingo") # Person.__init__("Kingo")
kingo.speak() # speak(kingo)
print kingo.height
