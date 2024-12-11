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
    new_arr = arr.copy()
    for i in range(len(new_arr)):
        if new_arr[i] == 0:
            print(f"element {new_arr[i]} changed to 1")
            new_arr[i] = 1
        else:
            if not even_num_digits(new_arr[i]):
                new_num = new_arr[i] * 2024
                print(f"element {new_arr[i]} changed to: {new_arr[i]} x 2024: {new_num}")
                new_arr[i] = new_num
    return new_arr

def split_elements(arr):
    new_arr = arr.copy()
#---------------------------

#---------------------------


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