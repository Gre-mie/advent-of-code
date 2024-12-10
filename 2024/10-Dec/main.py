def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read().split('\n')



#----- ----- ----- ----- ----- ----- -----

class Walker:
    def __init__(self, path, directions):
        self.directions = directions
        self.board = get_file(path)
        self.board_height = len(self.board)
        self.board_width = len(self.board[0])


        self.y = 0
        self.x = 0

        self.num = self.board[self.y][self.x] # number walker is standing on

        #current_path = []  # to store the past postions ?

    def check_if_on_board(self, y, x, height, width):
        if y < 0 or y > height:
            raise Exception(f"\033[31mWalker is off the board: \033[37;0m\n\033[33;2my:     {y}\nheight: {height}\033[37;0m")
        if x < 0 or x > width:
            raise Exception(f"\033[31mWalker is off the board: \033[37;0m\n\033[33;2mx:    {x}\nwidth: {width}\033[37;0m")

    def look(self, direction): # direction is a tuple
        look_y = self.directions[direction][0]
        look_x = self.directions[direction][1]

        #print(f"look y: {look_y}\nlook x: {look_x}\nboard height: {self.board_height}\nboard width: {self.board_width}\n")

        try:
            self.check_if_on_board(look_y, look_x, self.board_height, self.board_width)
        except Exception as message:
            print(message)

        return self.board[self.y + look_y][self.x + look_x]

    


#----- ----- ----- ----- ----- ----- -----


def main():

    directions = {
        "right": (0, +1),
        "down":  (+1, 0),
        "left":  (0, -1),
        "up":    (-1, 0)
               # (y , x)
    }
    
    p_walker = Walker("./puzzle-input.txt", directions)
    t_walker = Walker("./test-input.txt", directions)


#-------------------------------------------
    print(f"{t_walker.board}\n")

    for direction in directions:
        #print(f"walker:\ny: {t_walker.x}\nx: {t_walker.y}\nstanding on: {t_walker.num}\n")
        print(f"look {direction}:", t_walker.look(direction))
    
    
    print()
#-------------------------------------------

    advent_intro(2024, 10)






if __name__ == "__main__":
    main()