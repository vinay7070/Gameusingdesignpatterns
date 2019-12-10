from abc import ABC, abstractmethod
from random import randint
import types

# Abstract Player Class with Strategy Pattern
class StrategyPlayer(ABC):
    def __init__(self, func = None):
        if func is not None:
            self.display = types.MethodType(func, self)
    
    # Strategy Pattern Base Method
    def display(self, board):
        print('Display Parent Call')
        
    @abstractmethod
    def do_action(self, board):
        print('Starting Action')

# Human Class
class Human(StrategyPlayer):
    def do_action(self, board):
        super().do_action(board)
        while True:
            pos = int(input('Input Position 0 ~ 8: '))
            if board[pos] == '.':
                board[pos] = 'O'
                break
            print('Wrong Input, Please input again')

# Computer Class        
class Computer(StrategyPlayer):
    def do_action(self, board):
        super().do_action(board)
        while True:
            pos = randint(0, 8)
            if board[pos] == '.':
                board[pos] = 'X'
                print('Computer Selected ', pos)
                break

# Factory Class for Factory Design Pattern
class Factory:
    def getPlayer(self, player):
        if player == 'H':
            return Human(displayHuman)
        elif player == 'C':
            return Computer(displayComputer)

def displayHuman(self, board):
    print('Human Done')
    outStr = ''
    for i in range(0, 9):
        outStr += board[i] + ' '
        if i % 3 == 2:
            outStr += '\n'
    print(outStr)

def displayComputer(self, board):
    print('Computer Done')
    outStr = ''
    for i in range(0, 9):
        outStr += board[i] + ' '
        if i % 3 == 2:
            outStr += '\n'
    print(outStr)

# Main Game Class
class Game:
    def __init__(self):
        factory = Factory()
        self.players = []
        # Memento Pattern/Serialize
        self.players.append(factory.getPlayer('H'))
        self.players.append(factory.getPlayer('C'))
        self.board = ['.', '.', '.','.', '.', '.','.', '.', '.']
        self.turn = 0
        
    def checkWin(self):
        if self.board[0] != '.' and (self.board[0] == self.board[1] == self.board[2]
                                     or self.board[0] == self.board[3] == self.board[6] 
                                     or self.board[0] == self.board[4] == self.board[8]):
            return self.board[0]
        if self.board[1] != '.' and (self.board[1] == self.board[4] == self.board[7]):
            return self.board[1]
        if self.board[2] != '.' and (self.board[2] == self.board[4] == self.board[6] or self.board[2] == self.board[5] == self.board[8]):
            return self.board[2]
        if self.board[3] != '.' and (self.board[3] == self.board[4] == self.board[5]):
            return self.board[3]
        if self.board[6] != '.' and (self.board[6] == self.board[7] == self.board[8]):
            return self.board[6]
        for i in range(0, 9):
            if self.board[i] == '.':
                return '.'
        return 'D'
    
    def do_action(self):
        while self.checkWin() == '.':
            self.players[self.turn].do_action(self.board)
            self.players[self.turn].display(self.board)
            self.turn = 1 - self.turn
        winner = self.checkWin()
        if winner == 'O':
            print('Human Won!')
        elif winner == 'X':
            print('Computer Won!')
        else:
            print('Draw')
        
def main():
    game = Game()
    game.do_action()

main()
