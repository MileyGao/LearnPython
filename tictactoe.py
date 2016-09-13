class person(object):
    def __init__(self,name):
        self.name = name
       # self.type = persontype
    def personstep(self,n):
        print "player %s puts chess to > %r"%(self.name,n)

class chess(object):
    def __init__(self,chesstype):
        self.step = chesstype
    def chessstep(self,n):
        a[int(n)/10][int(n)%10] = self.step

miley = person('miley')
kingo = person ('kingo')
a = [['-' for i in range(0,3)] for j in range(0,3)]
mileychess = chess("o")
kingochess = chess("x")

def checkequal(jj):
    check=True
    for i in range(0,len(jj)):
        if jj[i]!=jj[0]:
            check = False
    if check and jj[0]!="-":
        return True
    else:
        return False


def checkwin(player):
    global aaa
    aaa = True
    for i in range(0,3):
        for j in range(0,3):
            #if (a[i][j] != a[i][2] or a[i][2] == "-") and (a[i][j]!=a[2][j] or a[2][j]=="-") and (a[i][i]!=a[j][j] or a[i][i]=="-") and (a[i][2-i]!=a[j][2-j] or a[i][2-i] =="-"):
             if checkequal(a[i]) or checkequal([a[k][i] for k in range(0,3)]) or checkequal([a[m][m] for m in range(0,3)]) or checkequal([a[mm][2-mm] for mm in range(0,3)]):
                print "%s  win"%player
                exit()
             else:
                aaa = False

def checkstep(m):
    checkstep = a[int(m)/10][int(m)%10] 
    global kk
    kk = m
    while checkstep == "o" or checkstep == "x":
       print "u have to change step" 
       m = raw_input(">") 
       checkstep = a[int(m)/10][int(m)%10] 
    kk = m

def printBoard(a):
    print "Current board:"
    for i in range(0,3):
        for j in range(0,3):
            print a[i][j],
        print ""
    
while True:
    n = raw_input("step of miley:")
    checkstep(n)
    miley.personstep(int(kk))
    mileychess.chessstep(int(kk))
    printBoard(a)
    checkwin('miley')

    bbb = True
    for i in range(0,3):
        for j in range(0,3):
            if a[i][j]=="-":
                bbb = False
    if bbb == True and aaa== False:
        print "tie"
        exit()

    n2 = raw_input("step of kingo:")
    checkstep(n2)
    kingo.personstep(int(kk))
    kingochess.chessstep(int(kk))
    printBoard(a)
    checkwin('kingo')
    
    bbb = True
    for i in range(0,3):
        for j in range(0,3):
            if a[i][j]=="-":
                bbb = False
    if bbb == True and aaa== False:
        print "tie"
        exit()
