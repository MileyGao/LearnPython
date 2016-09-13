class students(object):
    def __init__(self,name,height,grades):
        self.name = name
        self.height = height
        self.grades = grades
    def outputs(self):
        print "name:%s, height:%s, grades:%d "%(self.name,self.height,self.grades)
name = 'kingo'
a = students(name,'175',100)
#d = {"name":"kingo","height":}
a.outputs()

