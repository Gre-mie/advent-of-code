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
            print(f"change {num} to 1")
            new_arr.append(1)
            print(f"new array: {new_arr}\n")
        else:
            if even_num_digits(num):
                s_num = str(num)
                half = int(len(s_num) / 2)
                new_arr.append(int(s_num[:half]))
                new_arr.append(int(s_num[half:]))

                print(f"split: {num}")
                print(f"new array: {new_arr}\n")
            else:
                new_num = num * 2024
                print(f"element {num} changed to: {num} x 2024: {new_num}")
                new_arr.append(new_num)
                print(f"new array: {new_arr}\n")
    return new_arr


def run(times_to_run, file):
    stones_arr = file.copy()

    for i in range(times_to_run):
        stones_arr = change_elements(stones_arr)
#--------------------------------------------
        

#-------------------------------------------
        print(f"\nafter iteration {i+1}: {stones_arr}\n")
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