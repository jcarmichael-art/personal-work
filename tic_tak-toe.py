

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


#this just prints off all types of current posisions. this should be remade as a Board method later
    def x_turn2(self,board):
        print(f'x pos {self.x_pos(board)}')
        print(f'o pos {self.o_pos(board)}')
        print(f'pop pos {self.pos_pos(board)}')
#returns all x positions in a ["a1", "a2"] format
    def x_pos(self, board):
        x_pos = []
        for letter in board:
            for number in board[letter]:
                if board[letter][number] == "x":
                    x_pos.append(f"{letter}{number}")
        return x_pos
#returns all o postions in a ["a1", "a2"] format
    def o_pos(self, board):
        o_pos = []
        for letter in board:
            for number in board[letter]:
                if board[letter][number] == "o":
                    o_pos.append(f"{letter}{number}")
        return o_pos
#returns all possible postions in a ["a1", "a2"] format (SHOULD BE HELPFUL FOR MAKING THE AI)
    def pos_pos(self, board):
        pos_pos = []
        for letter in board:
            for number in board[letter]:
                if board[letter][number] == "_":
                    pos_pos.append(f'{letter}{number}')
        return pos_pos

#computer turns for if it is playing as x's or o's (currently not a feature, computer is always x's atm)
    def x_turn(self,board):
        letter, number = coord_validator(board)
        board[letter][number] = "x"

    def o_turn(self, board):
        letter, number = coord_validator(board)
        board[letter][number] = "o"

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
        for letter in self.board:
            for number in self.board[letter]:
                if self.board[letter][number] == "_":
                    pos_pos.append(f'{letter}{number}')
        return pos_pos

        
 #checks win condition, this is called in the main program and is not automatically ran when a turn happens (I may change this)
    def win_check(self):

        for player in self.players:
            #winner key (every stright line adds to 15, there is no possible combination that adds to 15 and isnt a win condition)
            convert_board = {"a1":8, "a2":1, "a3":6,
                            "b1":3, "b2":5, "b3":7,
                            "c1":4, "c2":9, "c3":2}
            win_num = []
            #convert all x positions into a list of ints
            if player.letter == "x":
                x_pos = self.x_pos()
                if len(x_pos) >= 3: 
                    for ele in x_pos:
                        if ele in convert_board:
                            win_num.append(convert_board[ele])


            elif player.letter == "o":
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
                                self.players[1].winner = True








    #checks win condition, this is called in the main program and is not automatically ran when a turn happens (I may change this)
    def x_win_check(self):

        #winner key (every stright line adds to 15, there is no possible combination that adds to 15 and isnt a win condition)
        convert_board = {"a1":8, "a2":1, "a3":6,
                         "b1":3, "b2":5, "b3":7,
                         "c1":4, "c2":9, "c3":2}
        
        #convert all x positions into a list of ints
        x_pos = self.players[1].x_pos(self.board)
        if len(x_pos) >= 3: 
            win_num = []
            for ele in x_pos:
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
                                self.players[1].winner = True


    #checks win condition, this is called in the main program and is not automatically ran when a turn happens (I may change this)
    def o_win_check(self):

        #winner key (every stright line adds to 15, there is no possible combination that adds to 15 and isnt a win condition)
        convert_board = {"a1":8, "a2":1, "a3":6,
                         "b1":3, "b2":5, "b3":7,
                         "c1":4, "c2":9, "c3":2}
        
        #convert all o positions into a list of ints
        o_pos = self.players[1].o_pos(self.board)
        if len(o_pos) >= 3: 
            win_num = []
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
                                self.players[0].winner = True

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
                 player.x_turn(board1.board)
                 board1.win_check()        
                 if player.winner == True:
                     break         
                 
            elif player.letter == "o":
                 player.o_turn(board1.board)
                 board1.win_check()
                 if player.winner == True:
                     break

        for player in board1.players:
            if player.winner == True:
                print(f'{player.name} is the winner!')



if __name__ == "__main__":
    main()