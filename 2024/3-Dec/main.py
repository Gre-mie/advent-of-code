def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_data(path):
    with open(path, 'r') as file:
        content = file.read()
        return content
    
def remove_invalid_chars(str):
    valid = "mul(,)0123456789"
    char_arr = []
    for char in str:
        if char in valid:
            char_arr.append(char)
    return "".join(char_arr)

def split_file_to_string_arr(file):
    string_array = []
    current_string = []
    possible_funct = False
    for char in file:
        if char == 'm':
            possible_funct = True
            current_string = []
            current_string.append(char)

        elif char == ')':
            current_string.append(char)

            if  len(current_string) >= 8:
                string_array.append("".join(current_string))

            possible_funct = False
            current_string = []

        elif possible_funct == True:
            current_string.append(char)
    print(f"string array:\n{string_array}")

    return string_array

def mul(i1, i2):
    return i1 * i2

def pull_args(funct_str):
    # return array of tuples, to be arguments for mul() function
    pass



def main():
    puzzle_file = split_file_to_string_arr(remove_invalid_chars(get_data("./puzzle-input.txt")))
    test_puzzle_file = split_file_to_string_arr(remove_invalid_chars(get_data("./test-puzzle-section.txt")))
    test_file = split_file_to_string_arr(remove_invalid_chars(get_data("./test-input.txt")))


    advent_intro(2024, 3)


#----------------------------
    print(f"TEST FILE:\n{test_file}")
    print("split file\n",test_file)

    test_args = pull_args(test_file)

    #print(f"TEST PUZZLE SECTION\n")
    #print("split file\n",test_puzzle_file)

    #test_puzzle_args = pull_args(test_puzzle_file)

    #print(f"PUZZLE FILE:\n")
    #print("split file\n", puzzle_file)

    #puzzle_args = pull_args(test_file)

    






#-------------------------------



if __name__ == "__main__":
    main()