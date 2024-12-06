def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def count_x(board):
    count = 0
    for line in board:
        for char in line:
            if char == 'X':
                count += 1
    return count

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda line: list(line), file.read().split('\n')))

def check_game_end(x, y, board_width, board_height):
    if x < 0 or x > board_width - 1:
        return True
    if y < 0 or y > board_height -1:
        return True
    return False

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
        ahead = ""
        if self.char == '^':
            if self.y - 1 < 0 or self.y - 1 > self.board_width - 1:
                return
            ahead = self.game_board[self.y - 1][self.x]
            #print(f"--- {self.char} | {ahead} ---")

        elif self.char == '>':
            if self.x + 1 < 0 or self.x - 1 > self.board_width + 1:
                return
            ahead = self.game_board[self.y][self.x + 1]
            #print(f"--- {self.char} | {ahead} ---")

        elif self.char == 'v':
            if self.y + 1 < 0 or self.y + 1 > self.board_width - 1:
                return
            ahead = self.game_board[self.y + 1][self.x]
            #print(f"--- {self.char} | {ahead} ---")

        elif self.char == '<':
            if self.x - 1 < 0 or self.x - 1 > self.board_width - 1:
                return
            ahead = self.game_board[self.y][self.x - 1]
            #print(f"--- {self.char} | {ahead} ---")

        else:
            raise Exception("\033[31mGuard not selected\033[37;0m")
        
        if ahead == '#':
            return "blocked"
        return

    def turn(self):
        turn = {
            '^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'
            }
        print("\033[33;2mturning...\033[37;0m")
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
        if check_game_end(self.x, self.y, self.board_width, self.board_height) == False:
            self.game_board[self.y][self.x] = self.char



#-----  -----   -----   -----   -----



def main():
    
    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    guard = Guard(test_file) # test arguments

    print(f"GUARD:\nx: {guard.x}\ny: {guard.y}\nchar: {guard.char}\n")
    print(f"BOARD WIDTH: {guard.board_width}\nBOARD HEIGHT: {guard.board_height}\n")

    print("GAME BOARD START:")
    guard.print_board()



#---------------------------------------
    advent_intro(2024, 6)
    

    
    
    game_end = False
    while game_end == False:
        print("\nchecking exit condition...")
        if check_game_end(guard.x, guard.y, guard.board_width, guard.board_height) == True:
            print(f"x: {guard.x}  width: {guard.board_width}\ny: {guard.y}  height: {guard.board_height}")
            print("EXITING GAME")
            game_end = True
            break
        else:
            print("game running...")
            guard.update()
            guard.print_board()

    print("--- --- --- FINAL BOARD --- --- ---")
    final_board = guard.game_board
    guard.print_board()

    answer(count_x(final_board))





if __name__ == "__main__":
    main()