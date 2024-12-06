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

def print_board(board):
    for line in board:
        print("".join(line))

def find_guard(board, board_width, board_height):
    for i in range(board_height):
        for j in range(board_width):
            char = board[i][j]
            match char:
                case '^':
                    return i, j, "up"
                case 'v':
                    return i, j, "down"
                case '<':
                    return i, j, "left"
                case '>':
                    return i, j, "right"     
    raise Exception("\033[31mGuard could not be found on the board:\033[93;2m find_guard(board)\033[37;0m")
                


#-----  -----   -----   -----   -----

class Guard:
    def __init__(self, x_y_direction_tuple, directions):
        self.x = x_y_direction_tuple[0]
        self.y = x_y_direction_tuple[1]

        self.direction = x_y_direction_tuple[2]
        self.char = directions[self.direction]
    
    def check_ahead(self, game_board):
        return "blocked" # test code
        return

    def turn(self):
        turn = {
            '^': ('>', "right"),
            '>': ('v', "down"),
            'v': ('<', "left"),
            '<': ('^', "up")
            }
        print("turning...")
        self.char = turn[self.char][0]
        self.direction = turn[self.char][1]

    def move(self, game_board):
        new_game_board = game_board.copy()
        if self.check_ahead(game_board) == "blocked":
            self.turn()
            new_game_board[self.x][self.y] = self.char

        
        return new_game_board


#-----  -----   -----   -----   -----



def main():
    
    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    BOARD_WIDTH = len(test_file)
    BOARD_HEIGHT = len(test_file[0])

    print(f"BOARD WIDTH: {BOARD_WIDTH}\nBOARD HEIGHT: {BOARD_HEIGHT}\n")

    directions = {
        "up":    '^',
        "down":  'v',
        "left":  '<',
        "right": '>'
    }

    game_board = test_file.copy() # TEST game board
    print("GAME BOARD START:\n", print_board(game_board))



#---------------------------------------
    advent_intro(2024, 6)
    
    guard = Guard(find_guard(game_board, BOARD_WIDTH, BOARD_HEIGHT), directions) # test arguments

    print(f"GUARD:\nx: {guard.x}\ny: {guard.y}\ndirection: {guard.direction}\nchar: {guard.char}")

    game_end = False
    #while game_end == False:
    for i in range(4): # test code
#        print("checking exit condition...") # test code
#        if check_game_end() == True:
 #           prin
  # t("EXITING GAME") # test code 
  #           break
        print("\ngame running...") # test code

        game_board = guard.move(game_board)

        # will need to update board before calling
        print_board(game_board)






if __name__ == "__main__":
    main()