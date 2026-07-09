
mydict = {"a":{1:"",2:"",3:""},
          "b":{1:"",2:"",3:""},
          "C":{1:"",2:"",3:""}}

def digit_checker(num):
    if num[0].isdigit():
        number = int(num[0])
        if num[1] is str:
            letter = num[1]
            return True, letter, number

    elif num[1].isdigit():
         number = int(num[1])
         if num[0] is str:
            letter = num[0]
            return True, letter, number
         
    else:
         return False, " ", " "

def coord_validator():
    while True:
        num = input("Enter coords > ")
        if len(num) == 2:
            print("lencheck")
            if num[0].isdigit():
                number = int(num[0])
                if num[1] in mydict and number in range(1,4):
                    letter = num[1]
                    return letter, number

            elif num[1].isdigit():
                number = int(num[1])
                if num[0] in mydict:
                    letter = num[0]
                    if letter == str and number == int:
                        return letter, number
        print("Invalid coords")
        
        

class Computer:
    def __init__(self,name):
        self.name = name

class Player:
     def __init__(self, name, letter, bool):
          self.name = name
          self.letter = letter
          self.winner = bool


class Board:
    def __init__(self):
        self.board = {"a":{1:"_",2:"_",3:"_"},
                      "b":{1:"_",2:"_",3:"_"},
                      "c":{1:"_",2:"_",3:"_"}}
        
    def x_turn(self, letter, number):
        is_num = digit_checker(number)
        self.board[letter][is_num] = "X"

    def o_turn(self,):
            coord = coord_validator()
            letter, number = coord

            self.board[letter][number] = "O"

    def print_board(self):
            print(f'  1 2 3')
            print(f'a {self.board["a"][1]} {self.board["a"][2]} {self.board["a"][3]}')
            print(f'b {self.board["b"][1]} {self.board["b"][2]} {self.board["b"][3]}')
            print(f'c {self.board["c"][1]} {self.board["c"][2]} {self.board["c"][3]}')


def main():

    player1 = Player("jake", "o", False)
    player2 = Player("gage", "x", False)
    players = [player1, player2]
    board1 = Board()

    while not player1.winner and not player2.winner:
        for player in players:
            board1.print_board()
            print(f"{player.name}'s turn, you are {player.letter}'s")
            if player.letter == "x":
                 board1.x_turn()
            elif player.letter == "o":
                 board1.o_turn()


    while not player1.winner and not player2.winner:
        if player1.letter == "x":
            board1.print_board()

            board1.x_turn(input("Enter letter column"),input("Enter number column"), player1.name)
        elif player2.letter == "o":
            board1.print_board()
            board1.o_turn(input("Enter letter column"),input("Enter number column", player2.name))
        if player1.letter == "x":
            board1.print_board()
            board1.x_turn(input("Enter letter column"),input("Enter number column"), player1.name)
        elif player2.letter == "o":
            board1.print_board()
            board1.o_turn(input("Enter letter column"),input("Enter number column", player2.name))
    print("test")


if __name__ == "__main__":
    main()