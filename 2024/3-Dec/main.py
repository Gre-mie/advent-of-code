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
    return string_array

def mul(i1, i2):
    return i1 * i2

def pull_args(funct_str_arr):
    arg_list = []
    for str in funct_str_arr:
        arg_array = str[4:-1].split(',')
        
        sub_list = []
        for item in arg_array:
            if item.isdigit():
                sub_list.append(int(item))
            else:
                break
        if sub_list != []:
            arg_list.append(sub_list)        
    return arg_list

def get_answer(args_list):
    total = 0
    for item in args_list:
        if len(item) > 1:
            a, b = item
            if a <= 999 and b <= 999:
                total += mul(a, b)
    return total


def main():
    puzzle_file = split_file_to_string_arr(remove_invalid_chars(get_data("./puzzle-input.txt")))
    #test_puzzle_file = split_file_to_string_arr(remove_invalid_chars(get_data("./test-puzzle-section.txt")))
    test_file = split_file_to_string_arr(remove_invalid_chars(get_data("./test-input.txt")))


    advent_intro(2024, 3)


#----------------------------
    print(f"TEST FILE:\n{test_file}")

    test_args = pull_args(test_file)
    print("test args:\n", test_args)

    answer(get_answer(test_args))

    
    test = split_file_to_string_arr(remove_invalid_chars(get_data("./test.txt")))

    print(f"TEST:\n{test}")
    t_args = pull_args(test)
    print("args:\n", t_args)

    answer(get_answer(t_args))
                                                      
                                            
    

    #print(f"TEST PUZZLE SECTION\n")

    #test_puzzle_args = pull_args(test_puzzle_file)
    #print("test puzzle args:\n", test_puzzle_args)

    print(f"PUZZLE FILE:\n")

    puzzle_args = pull_args(puzzle_file)
    print("puzzle args:\n", puzzle_args)
    answer(get_answer(puzzle_args))

    






#-------------------------------



if __name__ == "__main__":
    main()