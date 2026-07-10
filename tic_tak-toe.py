
from tkinter import *

#window = Tk()
#window.geometry("420x420")
#window.title("Tik_Tac_Toe")
#window.mainloop()

def coord_validator(board):
    while True:
        letter = None
        number = None
        num = input("Enter coords > ")
        for i in range(len(num)):
            if len(num) == 2:
                if num[i].isdigit() and number == None:
                    number = int(num[i])
                elif letter == None and num[i] in board:
                    letter = num[i]
        if number in range(0,4) and letter in board and board[letter][number] == "_":
            return letter, number    
        else:
            print("Invalid input")       
        

class Player:
    def __init__(self, name, winner):
        self.name = name
        self.winner = winner
        
class Computer(Player):
    def __init__(self,name,winner):
        super().__init__(name, winner)
        self.name = name
        self.winner = winner
        self.letter = "x"

    def x_turn(self,):
        letter, number = coord_validator(self.board)
        self.board[letter][number] = "X"

class Person(Player):

    def __init__(self, name, winner):
        super().__init__(name, winner)
        self.name = name
        self.winner  = winner
        self.letter = "o"

    def o_turn(self,):
        letter, number = coord_validator(self.board)
        self.board[letter][number] = "O"


class Board:
    def __init__(self):
        self.board = {"a":{1:"_",2:"_",3:"_"},
                      "b":{1:"_",2:"_",3:"_"},
                      "c":{1:"_",2:"_",3:"_"}}
        
    def x_turn(self,):
        letter, number = coord_validator(self.board)
        self.board[letter][number] = "X"

    def o_turn(self,):
        letter, number = coord_validator(self.board)
        self.board[letter][number] = "O"

    def print_board(self):
            print(f'  1 2 3')
            print(f'a {self.board["a"][1]} {self.board["a"][2]} {self.board["a"][3]}')
            print(f'b {self.board["b"][1]} {self.board["b"][2]} {self.board["b"][3]}')
            print(f'c {self.board["c"][1]} {self.board["c"][2]} {self.board["c"][3]}')


def main():

    person1 = Person("Jake", False)
    computa1 = Computer("computa", False)


    players = [person1, computa1]
    board1 = Board()
    while not person1.winner and not computa1.winner:
        for player in players:
            board1.print_board()
            print(f"{player.name}'s turn, you are {player.letter}'s")
            if player.letter == "x":
                 board1.x_turn()
            elif player.letter == "o":
                 board1.o_turn()

if __name__ == "__main__":
    main()