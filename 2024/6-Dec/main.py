def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda line: list(line), file.read().split('\n')))

def check_game_end():
    #if gaurd position x > board width -> board[0]
    #or
    #gaurd position y > board height -> board
    return True # game has ended guard has left the board

def find_guard(board, board_width, board_height):
    for x in range(board_height):
        for y in range(board_width):
            char = board[y][x]
            match char:
                case '^':
                    return x, y
                case 'v':
                    return x, y
                case '<':
                    return x, y
                case '>':
                    return x, y   
    raise Exception("\033[31mGuard could not be found on the board:\033[93;2m find_guard(board)\033[37;0m")
                


#-----  -----   -----   -----   -----

class Guard:
    def __init__(self, game_board):
        self.game_board = game_board.copy()
        self.board_width = len(self.game_board[0])
        self.board_height = len(self.game_board)

        self.x, self.y = find_guard(game_board, self.board_width, self.board_height)
        self.char = self.game_board[self.y][self.x]

    def print_board(self):
        for line in self.game_board:
            print("".join(line))
    
    def check_ahead(self):
        # can return "blocked"
        return

    def turn(self):
        turn = {
            '^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'
            }
        print("turning...")
        if self.char in turn:
            self.char = turn[self.char]
        else:
            raise Exception("\033[31mGuard not selected\033[37;0m")
        
    def move(self):
        self.game_board[self.y][self.x] = 'X'
        if self.char == '^':
            self.y -= 1
        elif self.char == '>':
            self.x += 1
        elif self.char == 'v':
            self.y += 1
        elif self.char == '<':
            self.x -= 1
        else:
            raise Exception("\033[31mGuard not selected\033[37;0m")

    def update(self):
        if self.check_ahead() == "blocked":
            self.turn()
        else:
            self.move()
        self.game_board[self.y][self.x] = self.char



#-----  -----   -----   -----   -----



def main():
    
    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    guard = Guard(test_file) # test arguments

    print(f"GUARD:\nx: {guard.x}\ny: {guard.y}\nchar: {guard.char}\n")
    print(f"BOARD WIDTH: {guard.board_width}\nBOARD HEIGHT: {guard.board_height}\n")

    

    #game_board = test_file.copy() # TEST game board
    print("GAME BOARD START:\n", guard.print_board())



#---------------------------------------
    advent_intro(2024, 6)
    

    

    game_end = False
    #while game_end == False:
    for i in range(3): # test code
#        print("checking exit condition...") # test code
#        if check_game_end() == True:
 #           prin
  # t("EXITING GAME") # test code 
  #           break
        print("\ngame running...") # test code

        guard.update()

        # will need to update board before calling
        guard.print_board()






if __name__ == "__main__":
    main()