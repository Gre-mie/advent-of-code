def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def format_data(line):
    first, second = line.split("   ")
    second = second.strip("\n")
    return first, second

def convert_string_array(data_array):
    list_1 = []
    list_2 = []
    for item in data_array:
        first, second = format_data(item)
        list_1.append(first)
        list_2.append(second)
    return list_1, list_2

def get_data_as_tuples(file_path):
    file = open(file_path)
    lines_array = file.readlines()
    return convert_string_array(lines_array)
        



def main():
    advent_intro(2024, 1)

    p_list_1, p_list_2 = get_data_as_tuples("./puzzle-input.txt")
    t_list_1, t_list_2 = get_data_as_tuples("./test-input.txt")

    

    #--------------
    

    print(f"TEST data:\nlist 1: {t_list_1}\nlist 2: {t_list_2}\n")
    #print(f"TEST data:\nlist 1: {p_list_1}\nlist 2: {p_list_2}\n")
    
    


    #---------------



if __name__ == "__main__":
    main()