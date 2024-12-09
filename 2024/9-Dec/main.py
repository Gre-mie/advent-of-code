def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda num: int(num) , file.read()))
    
def expand_element(element, index= -1):
    exp_el = []
    if index > -1:
        for i in range(element):
            exp_el.append(index)
    else:
        for i in range(element):
            exp_el.append('.')
    return exp_el

def expand_disc_map(file_arr):
    new_arr = []
    file_index = 0
    for i in range(len(file_arr)):
        if i % 2 == 0:
            new_arr += expand_element(file_arr[i], file_index)
            file_index += 1
        else:
            new_arr += expand_element(file_arr[i])
    return new_arr




def main():

    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    p_exp = expand_disc_map(get_file("./puzzle-input.txt"))
    t_exp = expand_disc_map(get_file("./test-input.txt"))

#--------------------------------------------------------

    print(f"{test_file}\n\n{t_exp}\n")



#--------------------------------------------------------


    advent_intro(2024, 9)






if __name__ == "__main__":
    main()