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

def run_game(object):
    game_end = False
    while game_end == False:
        if check_game_end(object.x, object.y, object.board_width, object.board_height) == True:
            game_end = True
            break
        else:
            object.update()
            #object.print_board()


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
        elif self.char == '>':
            if self.x + 1 < 0 or self.x - 1 > self.board_width + 1:
                return
            ahead = self.game_board[self.y][self.x + 1]
        elif self.char == 'v':
            if self.y + 1 < 0 or self.y + 1 > self.board_width - 1:
                return
            ahead = self.game_board[self.y + 1][self.x]
        elif self.char == '<':
            if self.x - 1 < 0 or self.x - 1 > self.board_width - 1:
                return
            ahead = self.game_board[self.y][self.x - 1]
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

    guard = Guard(puzzle_file)

    advent_intro(2024, 6)
    run_game(guard)
    final_board = guard.game_board

    answer(count_x(final_board))





if __name__ == "__main__":
    main()