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

def inc_dec_arr(data_item, arr_so_far):
    if len(data_item) < 2:
        return arr_so_far
    if data_item[0] > data_item[1]:
        arr_so_far.append("dec")
    elif data_item[0] < data_item[1]:
        arr_so_far.append("inc")
    elif data_item[0] == data_item[1]:
        arr_so_far.append("same")
    inc_dec_arr(data_item[1:], arr_so_far)
    return arr_so_far

def highest_num(data_item, highest):
    if len(data_item) < 2:
        return highest
    a, b = sorted([data_item[0], data_item[1]])
    difference = b - a
    if difference > highest:
        highest = difference
    return highest_num(data_item[1:], highest) 

def is_data_safe(data_item):
    comparison_arr = inc_dec_arr(data_item, [])
    highest_difference = highest_num(data_item, 0)
    if highest_difference > 3:
        return False
    if "same" in comparison_arr:
        return False
    if "dec" in comparison_arr and "inc" in comparison_arr:
        return False
    return True
    

def main():

    puzzle_input = get_lists("./puzzle-input.txt")
    test_input = get_lists("./test-input.txt")

    #print("\nTEST PUZZLE:\n",puzzle_input)
    #print("\nTEST INPUT:\n",test_input)

    advent_intro(2004, 2)
    count = 0
    for data in puzzle_input:
        if is_data_safe(data) == True:
            count += 1
    answer(count)

    advent_intro(2024, 2, 2)





if __name__ == "__main__":
    main()