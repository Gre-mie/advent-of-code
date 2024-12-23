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

def move_file_blocks(arr):
    new_arr = arr.copy()
    start = 0
    end = len(new_arr) - 1
    while start < end:
        if new_arr[start] == '.':
            if new_arr[end] != '.':
                new_arr[start] = new_arr[end]
                new_arr[end] = '.'
            else:
                start -= 1            
            end -= 1
        start += 1
    return new_arr

def get_checksum(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] != '.':
            total += i * arr[i]
        else:
            return total
        

def main():

    p_memory_blocks = move_file_blocks(expand_disc_map(get_file("./puzzle-input.txt")))
    t_memory_blocks = move_file_blocks(expand_disc_map(get_file("./test-input.txt")))

    advent_intro(2024, 9)
    answer(get_checksum(p_memory_blocks))

if __name__ == "__main__":
    main()