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

def check_string(str):
    print(str) #---------------------------------- working in this part ---------------
    return True

def split_file_to_string_arr(file):
    string_array = []
    current_string = []
    for char in file:
        if char == ')':
            current_string.append(char)
            str = "".join(current_string)
            if check_string(str) == True: # --------------- working in this part
                string_array.append(str)
            current_string = []
        else:
            current_string.append(char)
    print(f"string array:\n{string_array}")

    return string_array


def main():
    puzzle_file = remove_invalid_chars(get_data("./puzzle-input.txt"))
    test_puzzle_file = remove_invalid_chars(get_data("./test-puzzle-section.txt"))
    test_file = remove_invalid_chars(get_data("./test-input.txt"))


    advent_intro(2024, 3)

#----------------------------
    print(f"TEST FILE:\n")
    print("split file\n",split_file_to_string_arr(test_file))

    print(f"TEST PUZZLE SECTION\n")
    print("split file\n",split_file_to_string_arr(test_puzzle_file))

    #print(f"PUZZLE FILE:\n{puzzle_file}")

    






#-------------------------------



if __name__ == "__main__":
    main()