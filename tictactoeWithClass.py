class Board(object):
    def __init__(self):
        self.board = [['-' for i in range(0,3)] for j in range(0,3)]
    def output(self):
        """print the board"""
        for i in range(0,3):
            for j in range(0,3):
                print self.board[i][j],
            print ""
    def putChess(self,x,y,chessType):
        """
        put the chessType into (x,y) of the board
        return True if success, otherwise return False
        """
        if self.board[x][y] == '-':
            self.board[x][y] = chessType
            xx = False
        else:
            xx = True
    def winType(self,playername):
        """
        return who wins, 'o' or 'x'
        return '-' if no one wins for now
        """
        def checkequal(a):
            check = True
            for i in range(0,3):
                if a[i] != a[0]:
                    check = False
            if check and a[0] != "-":
                return True

        a = self.board
        for i in range(0,3):
                if checkequal(a[i]) or checkequal([a[k][i] for k in range(0,3)]) or checkequal([a[i][i]]) or checkequal([a[i][2-i]]):
                    print "%s wins"%playername  # use name print "%s wins"%self.name
                    exit()
                else:
                    return True
    def isTie(self):
        """
        return if the game is tie
        """
        isTie = True
        for i in range(0,3):
            for j in range(0,3):
                if a[i][j] == "-":
                    isTie = False
                    break
        if isTie == True and winType(self):
            print "tie"            
            exit()

class Player(object):
    def __init__(self,name,chessType):
        """
        chessType: 'o' or 'x'
        """
        self.name = name
        self.chessType = chessType
    def nextStep(self,board):
        """
        return [x,y] that indices
        """#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        global xx
        xx = True
        while xx == True:
            n = raw_input("step of %s:"%self.name)
            x = int(n)/10
            y = int(n)%10
            board.putChess(x,y,self.chessType)
            print "221"

class Game(object):
    def __init__(self):
        self.board = Board()#???????????????????????????????
    def startWithPlayer(self, player1, player2):
        while True:
            player1.nextStep(self.board)
            print "1"
            self.board.output()
            self.board.winType(player1.self.name)
            self.board.isTie()

            player2.nextStep(self.board)
            self.board.output()
            self.board.winType(player1.self.name)
            self.board.isTie()


game = Game()
player1 = Player('miley', 'o')
player2 = Player('kingo', 'x')
game.startWithPlayer(player1, player2)
