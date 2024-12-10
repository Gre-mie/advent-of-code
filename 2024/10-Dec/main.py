def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda row: list(map(lambda num: int(num) , row)) , file.read().split('\n')))


#-------------------------------------------

def run(walker, directions):
    print(f"{walker.board}\n")

    print(f"height: {walker.board_height}  width: {walker.board_width}")

    reached_end = False
# continues looking for a path untill the walker is standing on the last square, and path is empty
    while reached_end == False:
        if walker.path == [] and walker.y >= walker.board_height and walker.x >= walker.board_width:
            reached_end = True
        print(f"walker:\ny: {walker.y}  x: {walker.x}\npath = {walker.path}\n")


        for direction in directions:
            print(f"searching: {walker.searching_for}\nstanding: {walker.num}\n")

            if walker.y >= 0 and walker.y < walker.board_height - 1:
                if walker.x >= 0 and walker.x < walker.board_width - 1:
                    found = walker.look(direction)
                    print(f"look {direction}:", found)

        #if found == t_walker.searching_for:
         #   print(f"\nwalker standing on: {t_walker.searching_for}\n{found} is {direction}\n")

    # testing v
        if walker.x == walker.board_height:
            walker.y += 1
            walker.x = 0
        walker.x += 1
    # testing ^



#-------------------------------------------

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
        self.searching_for = 0

        self.path = [] # path traveled so far


    def check_if_on_board(self, y, x, height, width):
        if y < 0 or y > height:
            return False
            #raise Exception(f"\033[31mWalker is off the board: \033[37;0m\n\033[33;2my:     {y}\nheight: {height}\033[37;0m")
        if x < 0 or x > width:
            return False
            #raise Exception(f"\033[31mWalker is off the board: \033[37;0m\n\033[33;2mx:    {x}\nwidth: {width}\033[37;0m")
        return True

    def look(self, direction): # direction is a tuple
        look_y = self.directions[direction][0]
        look_x = self.directions[direction][1]
        
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

    run(t_walker, directions)

    advent_intro(2024, 10)






if __name__ == "__main__":
    main()