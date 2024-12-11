def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return list(map(lambda num: int(num) , file.read().split(' ')))
    
def change_zero_els(arr):
    new_arr = arr.copy()
    for i in range(len(new_arr)):
        if new_arr[i] == 0:
            new_arr[i] = 1
            print(f"element {new_arr[i]} changed to 1")
    return new_arr

def run(times_to_run, file):
    stones_arr = file.copy()

    for i in range(times_to_run):
        stones_arr = change_zero_els(stones_arr)
#--------------------------------------------

#-------------------------------------------
        print(f"after iteration {i+1}: {stones_arr}\n")
    return stones_arr

def main():

    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

    #print(puzzle_file)
    #print(test_file)

    test = [0, 1, 10, 99, 999]
    print(f"start: {test}\n")

#-----------------------------------------------
    print(f"final array:", run(2, test), '\n')

    advent_intro(2024, 11)





if __name__ == "__main__":
    main()