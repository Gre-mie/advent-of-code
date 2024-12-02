def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def split_lines_into_num_array(arr_of_str):
    num_arr = []
    for item in arr_of_str:
        num_arr.append(list(map(lambda num: int(num), item.split(' '))))
    return num_arr

def get_lists(path):
    file = open(path)
    lines_array = list(map(lambda item: item.strip('\n'), file.readlines()))
    return split_lines_into_num_array(lines_array)



def main():
    advent_intro(2004, 2)

    puzzle_input = get_lists("./puzzle-input.txt")
    test_input = get_lists("./test-input.txt")

    #print("\nTEST PUZZLE:\n",puzzle_input)
    print("\nTEST INPUT:\n",test_input)





if __name__ == "__main__":
    main()