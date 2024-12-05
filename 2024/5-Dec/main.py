def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read()

def split_to_tuple(str):
    arr = str.split('\n')
    new_arr = []
    for line in arr:
        new_arr.append(tuple(map(lambda num: int(num), line.split('|'))))
    return new_arr

def split_to_arrs_of_nums(str):
    arr = str.split('\n')
    new_arr = []
    for line in arr:
        new_arr.append(list(map(lambda num: int(num), line.split(','))))
    return new_arr





def main():
    
    puzzle_file = get_file("./puzzle-input.txt").split("\n\n")
    puzzle_first_sect, puzzle_second_sect = split_to_tuple(puzzle_file[0]), split_to_arrs_of_nums(puzzle_file[1])

    #print(f"PUZZLE: First section:\n{puzzle_first_sect}")
    #print(f"PUZZLE: Second section:\n{puzzle_second_sect}")

#------------------------------------------------------

    test_file = get_file("./test-input.txt").split("\n\n")
    test_first_sect, test_second_sect = split_to_tuple(test_file[0]), split_to_arrs_of_nums(test_file[1])

    print(f"TEST: First section:\n{test_first_sect}")
    print(f"TEST: Second section:\n{test_second_sect}")

    


    advent_intro(2024, 5)






if __name__ == "__main__":
    main()