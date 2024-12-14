from functions import *
from bot import Bot

def main():

    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    # width, height
    puzzle_grid = (101, 103)
    test_grid = (11, 7)

    test_bots = make_bots(test_file, test_grid)

    
    for bot in test_bots:
        print(bot)
        bot.print_grid()
    


    advent_intro(2024, 14)






if __name__ == "__main__":
    main()