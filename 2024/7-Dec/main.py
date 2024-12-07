def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read().split('\n')

def orginise_data(file):
    dic = {}
    for line in file:
        data = line.split(':')
        key = int(data[0])
        dic[key] = tuple(map(lambda num: int(num), data[1].strip().split(' ')))
    return dic

def add_all(arr):
    total = 0
    for num in arr:
        total += num
    return total

def check_for(func, dic):
    new_dic = dic.copy()
    valid = []
    for test_value, values in new_dic.items():
        if func(values) == test_value:
            valid.append(test_value)
    return valid
    
def remove_valid(valid_list, dic):
    new_dic = dic.copy()
    for key in valid_list:
        del new_dic[key]
    return new_dic


def main():
    
    puzzle_file = orginise_data(get_file("./puzzle-input.txt"))
    test_file = orginise_data(get_file("./test-input.txt"))

    advent_intro(2024, 7)
    equations = puzzle_file.copy()
    valid_equations = []

    valid_equations = check_for(add_all, equations)
    equations = remove_valid(valid_equations, equations) 
    
    print(valid_equations)
    answer(add_all(valid_equations))

#---------------------------------------------

# --- --- --- NOTES: --- --- ---
# I dont have much time today, but know the way I've started this is not going to work.

# A method and some sudo code for how I'd like to attempt this challenge again:
    # use - and / to reduce the test_value.
    # Will use recursion to try out the different possiblities
        # returns list of operators eg [+, *, *]
        # try operation, test_value - next num in list eg list[0]
            # if num after operation < 0
                # return to try a new path
            # else 
                # append '+' to list of operators
                # recurse with list[:-1], list of operators
        # try operation, test_value / next num in list eg list[0]
            # if num after operation < 0
                # return to try a new path
            # else 
                # append '*' to list of operators
                # recurse with list[:-1], list of operators


if __name__ == "__main__":
    main()