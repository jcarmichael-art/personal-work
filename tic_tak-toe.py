import random

#validate coordinates based on user input
#is able to capture input in a [a1] or [1a] format
def coord_validator_player(board):
    while True:
        letter = None
        number = None
        num = input("Enter coords > ").lower()
        #num = num.lower()
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


#computer's turn (x's turn)
    def x_turn(self,board):

        #get a list of all possible moves in a ["a1", "a2"] format
        possible_positions = board.pos_pos()

        #iterate through possible games, only goes one turn cycle atm. (I think I figured out how to implement a minimax algorithm for even better computer moves. will try it later.)
        #prioritizes quickest victory (prevents unneeded blocking moves)
        for move in possible_positions:
            letter = move[0]
            number = int(move[1])
            board.board[letter][number] = "x"
            if board.win_check("x"):              
                return
            board.board[letter][number] = "_"

        for move in possible_positions:
            letter = move[0]
            number = int(move[1])
            board.board[letter][number] = "o"
            if board.win_check("o"):         
                board.board[letter][number] = "x"     
                return
            board.board[letter][number] = "_"


        # if there are no winning or losing positions for the computer
        if board.win_check("x") != True:
            #pulls a random move from the current possible moves. Board method regenerates a updated list of possible moves every turn.
            board.board[letter][number] = "_"
            random_move = possible_positions[random.randint(0, len(possible_positions)-1)]
            letter = random_move[0]
            number = int(random_move[1])
            board.board[letter][number] = "x"
            return


#child of the player class
class Person(Player):

    def __init__(self, name, winner, letter):
        super().__init__(name, winner)
        self.name = name
        self.winner  = winner
        self.letter = letter

#person turns for if it is playing as x's or o's (currently not a feature, person is always o's atm)
    def x_turn(self,board):
        letter, number = coord_validator_player(board)
        board[letter][number] = "x"

    def o_turn(self, board):
        letter, number = coord_validator_player(board)
        board[letter][number] = "o"

        
class Board:
    def __init__(self):
        #inital board in a easy to read format
        self.board = {"a":{1:"_",2:"_",3:"_"},
                      "b":{1:"_",2:"_",3:"_"},
                      "c":{1:"_",2:"_",3:"_"}}
        
        #list of players to be referenced for other operations
        self.players = []

    #add players to the game, will need to be sure this is happening in the main program
    def add_player(self,player):
        self.players.append(player)

    #returns all x positions in a ["a1", "a2"] format
    def x_pos(self):
        x_pos = []
        x_pos.clear()
        for letter in self.board:
            for number in self.board[letter]:
                if self.board[letter][number] == "x":
                    x_pos.append(f"{letter}{number}")
        return x_pos
    #returns all o postions in a ["a1", "a2"] format
    def o_pos(self):
        o_pos = []
        o_pos.clear()
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

        #winner key (every stright line adds to 15(look up "magic square" if this make no sense), there is no possible combination that adds to 15 and isnt a win condition)
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


    #prints current board positions
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
    board1.add_player(computa1)
    board1.add_player(person1)


    while not person1.winner and not computa1.winner and len(board1.pos_pos()) != 0:

        for player in board1.players:
            board1.print_board()

            if len(board1.pos_pos()) == 0:
                 print("It's a tie!")

            elif player.letter == "x":
                 print(f"{player.name}'s turn, you are {player.letter}'s")
                 player.x_turn(board1)
                 if board1.win_check("x"):        
                     player.winner = True
                     board1.print_board()
                     print(f'{player.name} is the winner!')
                     break         
                 
            elif player.letter == "o":
                 print(f"{player.name}'s turn, you are {player.letter}'s")
                 player.o_turn(board1.board)
                 if board1.win_check("o"):
                     player.winner = True
                     board1.print_board()
                     print(f'{player.name} is the winner!')
                     break

if __name__ == "__main__":
    main()