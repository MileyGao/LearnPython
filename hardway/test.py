def init(name):
    a = {}
    a["name"] = name
    return a
def speak(self):
    print "my name is:",self["name"]

kingo = init("Kingo")
speak(kingo)
