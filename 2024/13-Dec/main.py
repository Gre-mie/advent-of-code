from classArcade import Arcade

def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read().split('\n')


def main():

    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    puzzle = Arcade(puzzle_file)
    test = Arcade(test_file)

    print(test.process_file())

    advent_intro(2024, 13)






if __name__ == "__main__":
    main()