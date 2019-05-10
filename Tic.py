# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:56:04 2019

@author: RNSmith
"""



class Board():
    
    X_MOVE = True #X goes first
    
    def __init__(self):

        self.grid = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
            '5': ' ',
            '6': ' ',
            '7': ' ',
            '8': ' ',
            '9': ' ',}
    def display(self):
        print(' '+ self.grid['1'] + '|' + self.grid['2'] + '|' + self.grid['3'])
        print('--+-+--')
        print(' '+self.grid['4'] + '|' + self.grid['5'] + '|' + self.grid['6'])
        print('--+-+--')    
        print(' '+self.grid['7'] + '|' + self.grid['8'] + '|' + self.grid['9']) 
   
    def checkWinner(self):
        #Checking horizontals
        if(self.grid['1'] == self.grid['2'] and self.grid['2'] == self.grid['3'] and self.grid['1'] != ' '):
            return True
        elif(self.grid['4'] == self.grid['5'] and self.grid['4'] == self.grid['6'] and self.grid['4'] != ' '):
            return True
        elif(self.grid['7'] == self.grid['8'] and self.grid['7'] == self.grid['9'] and self.grid['7'] != ' '):
            return True 
        #Checking verticals
        elif(self.grid['1'] == self.grid['4'] and self.grid['1'] == self.grid['7'] and self.grid['1'] != ' '):
            return True        
        elif(self.grid['2'] == self.grid['5'] and self.grid['2'] == self.grid['8'] and self.grid['2'] != ' '):
            return True           
        elif(self.grid['3'] == self.grid['6'] and self.grid['3'] == self.grid['9'] and self.grid['3'] != ' '):
           return True           
       #Checking diagonals
        elif(self.grid['1'] == self.grid['5'] and self.grid['1'] == self.grid['9'] and self.grid['1'] != ' '):
            return True           
        elif(self.grid['3'] == self.grid['5'] and self.grid['3'] == self.grid['7'] and self.grid['3'] != ' '):
            return True           
        else:
            return False
    
    def checkDraw(self):
        for x in self.grid.keys():
            if(self.grid[x] == ' '):
                return False
        return True
    
    def legalMove(self, x):
        if(self.grid[x] != ' '):
            return False
        else:
            return True
    
    def move(self):
        if(self.X_MOVE):
            print('X\'s Move: ')
        else:
            print('O\'s Move: ')
        userInput = input()
        if(userInput in self.grid.keys()):
            if(self.X_MOVE and self.legalMove(userInput)):
                self.grid[userInput] = 'x'
                self.X_MOVE = False
            elif(self.legalMove(userInput)):
                self.grid[userInput] = 'o'
                self.X_MOVE = True
            else:
                print('Invalid Move')
        else:
            print('Invalid Move')
            self.move()
            
    
    def play(self):
        while True:
            self.display()
            self.move()
            if(self.checkWinner()):
                self.display()
                
                if(not self.X_MOVE):
                    print('X Wins')
                    break
                else:
                    print('O Wins')
                    break
            elif(self.checkDraw()):
                self.display()
                print('Draw')
                break
            
            
testBoard = Board()
testBoard.play()
    
    


