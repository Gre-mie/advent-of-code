def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda num: int(num) , file.read().split(' ')))
    
def even_num_digits(num):
    n = str(num)
    if len(n) % 2 == 0:
        return True
    return False
    
def change_elements(arr):
    new_arr = []
    for num in arr:
        if num == 0:
            new_arr.append(1)
        else:
            if even_num_digits(num):
                s_num = str(num)
                half = int(len(s_num) / 2)
                new_arr.append(int(s_num[:half]))
                new_arr.append(int(s_num[half:]))
            else:
                new_num = num * 2024
                new_arr.append(new_num)
    return new_arr

def run(times_to_run, file):
    stones_arr = file.copy()
    if times_to_run <= 25:
        for i in range(times_to_run):
            stones_arr = change_elements(stones_arr)
        return stones_arr
    else:
        raise Exception("\033[31m Do NOT run this code more then 25 iterations: \033[33;2mException in run(times_to_run, file)\033[37;0m")

def main():

    #puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    advent_intro(2024, 11)
    answer(len(run(25, get_file("./puzzle-input.txt"))))

    # !!!!! Do NOT run this code above 25 !!!!!


if __name__ == "__main__":
    main()