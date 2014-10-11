#! /usr/bin/python

class Tictactoe(object):
    def __init__(self):
        self.board = []
        self.num_empty = 9
        for y in range(3):
            row = []
            for x in range(3):
                row.append("")
            self.board.append(row)

    def play(self):
        while ( self.checkWinning() is 0 and self.num_empty is not 0):
            self.drawBoard()
            row, col = input("row, col : ")
            while not ( row >= 0 and row < 3 and col >= 0 and col < 3 ):
                row, col = input("row, col : ")
            try:
                self.putX(row, col)
            except ValueError:
                print "invalid move. try another spot"
                continue
            try :
                ai_response = self.findBestMove(1)
            except ValueError:
                continue
            self.putO(ai_response['row'], ai_response['col'])
        if ( self.checkWinning() is 1 ):
            self.drawBoard()
            print "Player Won!"
        elif ( self.checkWinning() is -1 ):
            self.drawBoard()
            print "Computer won!"
        else:
            self.drawBoard()
            print "Draw game!"


    def findBestMove(self, turn):
        if ( self.num_empty is 0 ):
            raise ValueError("already ended game")
        else:
            if ( turn is 0 ):
                maximum = -1 
                bestmove = {}
                results = []
                for row in range(3):
                    for col in range(3):
                        if ( self.board[row][col] is ""):
                            self.putX(row, col)
                            if ( self.checkWinning() is 1 ):
                                self.remove(row,col)
                                return {'row': row, 'col': col}
                            value = self.getValue(1)
                            self.remove(row,col)
                            result = {'value': value, 'move': {'row': row, 'col': col}}
                            results.append(result)
                for each_result in results:
                    if ( each_result['value'] >= maximum ):
                        maximum = each_result['value']
                        bestmove = each_result['move']
                return bestmove
            else: 
                minimum = 1 
                bestmove = {}
                results = []
                for row in range(3):
                    for col in range(3):
                        if ( self.board[row][col] is ""):
                            self.putO(row, col)
                            if ( self.checkWinning() is -1 ):
                                self.remove(row, col)
                                return {'row': row, 'col': col}
                            value = self.getValue(0)
                            self.remove(row,col)
                            result = {'value': value, 'move': {'row': row, 'col': col}}
                            results.append(result)
                for each_result in results:
                    if ( each_result['value'] <= minimum ):
                        minimum = each_result['value']
                        bestmove = each_result['move']
                return bestmove
            
    """ finds the value of the current game """
    def getValue(self, turn): # turn: 0/1 indicates X/O's turn
        result = self.checkWinning()
        if ( result == 1 ):
            return 1 # X's win
        elif ( result == -1 ): 
            return -1 # O's 
        elif ( self.num_empty == 0 and result == 0 ):
            return 0 # draw game
        else:
            if turn is 0: # X's turn
                results = []
                for row in range(3):
                    for col in range(3):
                        if ( self.board[row][col] is ""):
                            self.putX(row,col)
                            result = self.getValue(1)
                            results.append(result)
                            self.remove(row,col)
                return max(results)
            else: # O's turn
                results = []
                for row in range(3):
                    for col in range(3):
                        if ( self.board[row][col] is ""):
                            self.putO(row,col)
                            result = self.getValue(0)
                            results.append(result)
                            self.remove(row,col)
                return min(results)
        

    def putO(self, row, col):
        if not ( self.board[row][col] == ""):
            raise ValueError("already occupied spot!")
        else:
            self.board[row][col] = "O"
            self.num_empty -= 1
            won = self.checkWinning()
            return won
            #if ( won == 1 ):
             #   print "O won the game!"

    def putX(self, row, col):
        if not ( self.board[row][col] == ""):
            raise ValueError("already occupied spot!")
        else:
            self.board[row][col] = "X"
            self.num_empty -= 1
            won = self.checkWinning()
            return won
            #if ( won == -1 ):
             #   print "X won the game!"
    def remove(self, row, col):
        if ( self.board[row][col] == ""):
            raise ValueError("already empty spot!")
        else:
            self.board[row][col] = ""
            self.num_empty += 1

    def printStat(self):
        print self.board

    def drawBoard(self):
        print "    0   1   2  "
        print "0 |%2s |%2s |%2s |" %(self.board[0][0], self.board[0][1], self.board[0][2])
        print "  -------------"
        print "1 |%2s |%2s |%2s |" %(self.board[1][0], self.board[1][1], self.board[1][2])
        print "  -------------"
        print "2 |%2s |%2s |%2s |" %(self.board[2][0], self.board[2][1], self.board[2][2])



    def checkWinning(self):
        # check rows
        for row in self.board:
            result = ''
            for spot in row:
                result += spot
            if ( result == "OOO" ):
                return -1 # O wins
            elif ( result == "XXX" ):
                return 1 # X wins
        # check cols
        for col in range(3):
            result = ''
            for i in range(3):
                result += self.board[i][col]
            if ( result == "OOO" ):
                return -1 # O wins
            elif ( result == "XXX" ):
                return 1 # X wins
        # check diag
        diag = ( self.board[0][0] + self.board[1][1] + self.board[2][2])
        rdiag = ( self.board[0][2] + self.board[1][1] + self.board[2][0])
        if ( diag == "OOO" or rdiag == "OOO"):
            return -1
        elif ( diag == "XXX" or rdiag == "XXX" ):
            return 1
        return 0 # no won has won yet


if __name__ == '__main__':
    game = Tictactoe()
    game.play()


    
