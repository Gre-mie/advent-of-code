def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda num: int(num) , file.read().split(' ')))


def main():

    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    print(puzzle_file)
    print(test_file)



    advent_intro(2024, 11)






if __name__ == "__main__":
    main()