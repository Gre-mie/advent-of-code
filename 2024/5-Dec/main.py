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
    
def find_rule(num, rules):
    rules_found = []
    for rule in rules:
        a, b = rule
        if num == a or num == b:
            rules_found.append(rule) 
    return rules_found

def get_indexs(rule, update):
    first, second = rule
    if first in update:
        index_1 = update.index(first)
    else:
        index_1 = '-'
    if second in update:
        index_2 = update.index(second)
    else:
        index_2 = '-'
    return index_1, index_2

def check_updates(updates_arr, rules):
    correct_updates = updates_arr.copy()
    for i in range(len(updates_arr) -1):
        update = updates_arr[i]
        print(update)
        for num in update:
            relevent_rules = find_rule(num, rules)
            if not relevent_rules == []:
                for rule in relevent_rules:
                    indexs = get_indexs(rule, update)
                    #print(f"index 1: {indexs[0]}\nindex 2: {indexs[1]}\n")
                    if not '-' in indexs:
                        a, b = indexs
                        if a > b:
                            print("------------ bad update ----------------")
                            if update in correct_updates:
                                correct_updates.remove(update)
    return correct_updates

def get_answer(correct_arr):
    count = 0
    for update in correct_arr:
        count += update[int(len(update) / 2)]
    return count


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

    # Note: The last update in correct updates should not be added to the array :/
    
    #print("\nTEST: correct updates:\n", correct_updates)

#--------------------------------------------------------  
    advent_intro(2024, 5)
    answer(get_answer(check_updates(t_updates_arr, t_rules)))


if __name__ == "__main__":
    main()