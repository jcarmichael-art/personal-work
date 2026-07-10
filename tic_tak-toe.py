
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
    def __init__(self,name,winner,letter):
        super().__init__(name, winner)
        self.name = name
        self.winner = winner
        self.letter = letter

    def x_turn2(self,board):
        print(f'x pos {self.x_pos(board)}')
        print(f'o pos {self.o_pos(board)}')
        print(f'pop pos {self.pos_pos(board)}')
        

    def x_pos(self, board):
        x_pos = []
        for letter in board:
            for number in board[letter]:
                if board[letter][number] == "x":
                    x_pos.append(f"{letter}{number}")
        return x_pos
    

    def o_pos(self, board):
        o_pos = []
        for letter in board:
            for number in board[letter]:
                if board[letter][number] == "o":
                    o_pos.append(f"{letter}{number}")
        return o_pos


    def pos_pos(self, board):
        pos_pos = []
        for letter in board:
            for number in board[letter]:
                if board[letter][number] == "_":
                    pos_pos.append(f'{letter}{number}')
        return pos_pos


    def x_turn(self,board):
        letter, number = coord_validator(board)
        board[letter][number] = "x"

    def o_turn(self, board):
        letter, number = coord_validator(board)
        board[letter][number] = "o"


class Person(Player):

    def __init__(self, name, winner, letter):
        super().__init__(name, winner)
        self.name = name
        self.winner  = winner
        self.letter = letter

    def x_turn(self,board):
        letter, number = coord_validator(board)
        board[letter][number] = "x"

    def o_turn(self, board):
        letter, number = coord_validator(board)
        board[letter][number] = "o"

        


class Board:
    def __init__(self):
        self.board = {"a":{1:"_",2:"_",3:"_"},
                      "b":{1:"_",2:"_",3:"_"},
                      "c":{1:"_",2:"_",3:"_"}}
        self.players = []

    def add_player(self,player):
        self.players.append(player)
        
    def x_win_check(self):
        convert_board = {"a1":8, "a2":1, "a3":6,
                         "b1":3, "b2":5, "b3":7,
                         "c1":4, "c2":9, "c3":2}
        
        x_pos = self.players[1].x_pos(self.board)
        if len(x_pos) >= 3: 
            win_num = []
            for ele in x_pos:
                if ele in convert_board:
                    win_num.append(convert_board[ele])

            for i in range(len(win_num)):
                for j in range(len(win_num)):
                    for k in range(len(win_num)):
                        if i + 2 < len(win_num):
                            if win_num[i] + win_num[j] + win_num[k] == 15 and i != j != k != i:
                                self.players[1].winner = True

    def o_win_check(self):
        convert_board = {"a1":8, "a2":1, "a3":6,
                         "b1":3, "b2":5, "b3":7,
                         "c1":4, "c2":9, "c3":2}
        
        o_pos = self.players[1].o_pos(self.board)
        if len(o_pos) >= 3: 
            win_num = []
            for ele in o_pos:
                if ele in convert_board:
                    win_num.append(convert_board[ele])

            for i in range(len(win_num)):
                for j in range(len(win_num)):
                    for k in range(len(win_num)):
                        if i + 2 < len(win_num):
                            if win_num[i] + win_num[j] + win_num[k] == 15 and i != j != k != i:
                                self.players[0].winner = True


    def print_board(self):
            print(f'  1 2 3')
            print(f'a {self.board["a"][1]} {self.board["a"][2]} {self.board["a"][3]}')
            print(f'b {self.board["b"][1]} {self.board["b"][2]} {self.board["b"][3]}')
            print(f'c {self.board["c"][1]} {self.board["c"][2]} {self.board["c"][3]}')


def main():
    person1 = Person("Jake", False, "o")
    computa1 = Computer("computa", False, "x")

    board1 = Board()
    board1.add_player(person1)
    board1.add_player(computa1)


    while not person1.winner and not computa1.winner:
        for player in board1.players:
            board1.print_board()
            print(f"{player.name}'s turn, you are {player.letter}'s")
            if player.letter == "x":
                 #player.x_turn2(board1.board)
                 player.x_turn(board1.board)
                 board1.x_win_check()        
                 if player.winner == True:
                     break         
                 
            elif player.letter == "o":
                 player.o_turn(board1.board)
                 board1.o_win_check()
                 if player.winner == True:
                     break

        for player in board1.players:
            if player.winner == True:
                print(f'{player.name} is the winner!')
if __name__ == "__main__":
    main()