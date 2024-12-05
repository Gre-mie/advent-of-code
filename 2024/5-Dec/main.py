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

def is_odd(arr_of_num):
        if len(arr_of_num) % 2 != 0:
            return True
        else:
            return False

def check_lines_are_odd(arr_of_lines):
    all_odd = True
    for line in arr_of_lines:
        if not is_odd(line):
            print("\033[31m Even number of elements:\033[37m", len(line))
            print(line)
            all_odd = False
    if all_odd:
        return f"\033[33mAll arrays have an ODD number of elements\033[37m"
    else:
        return f"\033[33mSome arrays have an EVEN number of elements\033[37m"



def main():
    
    puzzle_file = get_file("./puzzle-input.txt").split("\n\n")
    p_rules, p_updates_arr = split_str(puzzle_file[0], '|', tuple), split_str(puzzle_file[1], ',', list)
    print("PUZZLE: second section:", check_lines_are_odd(p_updates_arr))

    #print(f"PUZZLE: First section:\n{p_rules}\n")
    #print(f"PUZZLE: Second section:\n{p_updates_arr}\n")

#------------------------------------------------------

    test_file = get_file("./test-input.txt").split("\n\n")
    t_rules, t_updates_arr = split_str(test_file[0], '|', tuple), split_str(test_file[1], ',', list)
    print("TEST:   second section:", check_lines_are_odd(t_updates_arr))

    print(f"TEST: First section:\n{t_rules}\n")
    print(f"TEST: Second section:\n{t_updates_arr}\n")



#--------------------------------------------------------


# Function: check if update is in correct order
# Run once, check for correct updates in array : use sort updates method
        # return correct arrays
        # remove correct arrays from array of updates to validate

# loop correct arrays adding together the middle numbers
        # print answer
                # result should be '143'


        #!!!!!! DO NOT SORT THE UPDATES !!!!!!!!!!
# sort updates in array of updates to vaildate
        # in each update, 
            # num of swaps = 0
            # check if number is in tuples
                # if in tuples, check if second number in tuple is in update
                                                    # get its index
                # check if index of current num and saved num are in correct order
                        # if not, swap the numbers using their indexs
                                    # num of swaps + 1
            # if num of swaps = 0 add update to correct arrays
    
                        

#--------------------------------------------------------  

    
    


    advent_intro(2024, 5)






if __name__ == "__main__":
    main()