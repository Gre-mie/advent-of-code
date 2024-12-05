def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read()

def split_str(str, split_by, funct):
    arr = str.split('\n')
    new_arr = []
    for line in arr:
        new_arr.append(funct(map(lambda n: int(n), line.split(split_by))))
    return new_arr




def main():
    
    puzzle_file = get_file("./puzzle-input.txt").split("\n\n")
    puzzle_first_sect, puzzle_second_sect = split_str(puzzle_file[0], '|', tuple), split_str(puzzle_file[1], ',', list)

    #print(f"PUZZLE: First section:\n{puzzle_first_sect}\n")
    #print(f"PUZZLE: Second section:\n{puzzle_second_sect}\n")

#------------------------------------------------------

    test_file = get_file("./test-input.txt").split("\n\n")
    test_first_sect, test_second_sect = split_str(test_file[0], '|', tuple), split_str(test_file[1], ',', list)

    print(f"TEST: First section:\n{test_first_sect}\n")
    print(f"TEST: Second section:\n{test_second_sect}\n")

    


    advent_intro(2024, 5)






if __name__ == "__main__":
    main()