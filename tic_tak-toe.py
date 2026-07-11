import random

#validate coordinates no matter input
def coord_validator(board):
    while True:
        letter = None
        number = None
        num = input("Enter coords > ")
        #general input validation
        for i in range(len(num)):
            if len(num) == 2:
                if num[i].isdigit() and number == None:
                    number = int(num[i])
                elif letter == None and num[i] in board:
                    letter = num[i]
        #final input validation. prevents instances of ab or 12
        if number in range(0,4) and letter in board and board[letter][number] == "_":
            return letter, number    
        else:
            print("Invalid input")       


def coord_validator2(board, num, random_):
    while True:
        if random_ == True:
            letters = "abc"
            random1 = random.randint(0,2)
            random2 = random.randint(1,3)
            random2 = str(random2)
            num = letters[random1] + random2
    
        letter = None
        number = None
        #general input validation
        for i in range(len(num)):
            if len(num) == 2:
                if num[i].isdigit() and number == None:
                    number = int(num[i])
                elif letter == None and num[i] in board:
                    letter = num[i]
        #final input validation. prevents instances of ab or 12
        if number in range(0,4) and letter in board and board[letter][number] == "_":
            return letter, number    
        
#parent class of all players
class Player:
    def __init__(self, name, winner):
        self.name = name
        self.winner = winner

#child of player class
class Computer(Player):
    def __init__(self,name,winner,letter):
        super().__init__(name, winner)
        self.name = name
        self.winner = winner
        self.letter = letter


#computer turns for if it is playing as x's or o's (currently not a feature, computer is always x's atm)
    def x_turn(self,board):
        possible_positions = board.pos_pos()

        for move in possible_positions:
            letter, number = coord_validator2(board.board, move, False)
            board.board[letter][number] = "x"
            if board.win_check("x"):
                break
            else:
                board.board[letter][number] = "_"
                print("test1")

        if not board.win_check("x"):
    
            letter, number = coord_validator2(board.board, None, True)
            board.board[letter][number] = "x"


                
            
        





#child of the player class
class Person(Player):

    def __init__(self, name, winner, letter):
        super().__init__(name, winner)
        self.name = name
        self.winner  = winner
        self.letter = letter

#person turns for if it is playing as x's or o's (currently not a feature, person is always o's atm)
    def x_turn(self,board):
        letter, number = coord_validator(board)
        board[letter][number] = "x"

    def o_turn(self, board):
        letter, number = coord_validator(board)
        board[letter][number] = "o"

        


class Board:
    def __init__(self):
        #inital board in a easy to read format
        self.board = {"a":{1:"x",2:"_",3:"_"},
                      "b":{1:"x",2:"_",3:"_"},
                      "c":{1:"_",2:"_",3:"_"}}
        
        #list of players to be referenced for other operations
        self.players = []

    #add players to the game, will need to be sure this is happening in the main program
    def add_player(self,player):
        self.players.append(player)

    #returns all x positions in a ["a1", "a2"] format
    def x_pos(self):
        x_pos = []
        for letter in self.board:
            for number in self.board[letter]:
                if self.board[letter][number] == "x":
                    x_pos.append(f"{letter}{number}")
        return x_pos
    #returns all o postions in a ["a1", "a2"] format
    def o_pos(self):
        o_pos = []
        for letter in self.board:
            for number in self.board[letter]:
                if self.board[letter][number] == "o":
                    o_pos.append(f"{letter}{number}")
        return o_pos
    #returns all possible postions in a ["a1", "a2"] format (SHOULD BE HELPFUL FOR MAKING THE AI)
    def pos_pos(self):
        pos_pos = []
        pos_pos.clear()
        for letter in self.board:
            for number in self.board[letter]:
                if self.board[letter][number] == "_":
                    pos_pos.append(f'{letter}{number}')
        return pos_pos

        
 #checks win condition, this is called in the main program and is not automatically ran when a turn happens (I may change this)
    def win_check(self, letter):


        #winner key (every stright line adds to 15, there is no possible combination that adds to 15 and isnt a win condition)
        convert_board = {"a1":8, "a2":1, "a3":6,
                        "b1":3, "b2":5, "b3":7,
                        "c1":4, "c2":9, "c3":2}
        win_num = []
        #convert all x positions into a list of ints
        if letter == "x":
            x_pos = self.x_pos()
            if len(x_pos) >= 3: 
                for ele in x_pos:
                    if ele in convert_board:
                        win_num.append(convert_board[ele])

        #convert all o positions into a list of ints
        elif letter == "o":
            o_pos = self.o_pos()
            if len(o_pos) >= 3: 
                for ele in o_pos:
                    if ele in convert_board:
                        win_num.append(convert_board[ele])               

        # check if there is a combination of 3 unique ints that add to 15
        for i in range(len(win_num)):
            for j in range(len(win_num)):
                for k in range(len(win_num)):
                    #prevents indexing out of range
                    if i + 2 < len(win_num):
                        #checks to be sure none of the numbers are of the same index value
                        if win_num[i] + win_num[j] + win_num[k] == 15 and i != j != k != i:
                            return True
        return False


    #prints updated board positions
    def print_board(self):
            print(f'  1 2 3')
            print(f'a {self.board["a"][1]} {self.board["a"][2]} {self.board["a"][3]}')
            print(f'b {self.board["b"][1]} {self.board["b"][2]} {self.board["b"][3]}')
            print(f'c {self.board["c"][1]} {self.board["c"][2]} {self.board["c"][3]}')


def main():
    #create players
    person1 = Person("Jake", False, "o")
    computa1 = Computer("computa", False, "x")

    #create board and add players to it
    board1 = Board()
    board1.add_player(person1)
    board1.add_player(computa1)


    while not person1.winner and not computa1.winner:

        for player in board1.players:
            board1.print_board()
            print(f"{player.name}'s turn, you are {player.letter}'s")
            if player.letter == "x":
                 player.x_turn(board1)
                 if board1.win_check("x"):        
                     player.winner = True
                     break         
                 
            elif player.letter == "o":
                 player.o_turn(board1.board)
                 if board1.win_check("o"):
                     player.winner = True
                     break

        for player in board1.players:
            if player.winner == True:
                board1.print_board()
                print(f'{player.name} is the winner!')



if __name__ == "__main__":
    main()