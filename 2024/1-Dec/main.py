def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def format_data(line):
    first, second = line.split("   ")
    second = second.strip("\n")
    return first, second

def convert_string_array_to_lists(data_array):
    list_1 = []
    list_2 = []
    for item in data_array:
        first, second = format_data(item)
        list_1.append(int(first))
        list_2.append(int(second))
    return list_1, list_2

def get_lists(file_path):
    file = open(file_path)
    lines_array = file.readlines()
    return convert_string_array_to_lists(lines_array)

def find_difference(min_1, min_2):    
    smallest = sorted([min_1, min_2])
    return smallest[1] - smallest[0]
        
def add(list):
        count = 0
        for n in list:
            count += n
        return count

def answer(differences):
    total = add(differences)
    return f"ANSWER: {total}"

def create_differences_list(list_1, list_2, differences):
    for _ in range(len(list_1)):
        smallest_in_list_1 = min(list_1)
        smallest_in_list_2 = min(list_2)
        differences.append(find_difference(smallest_in_list_1, smallest_in_list_2))
        list_1.remove(smallest_in_list_1)
        list_2.remove(smallest_in_list_2)
    return list_1, list_2, differences


def main():
    advent_intro(2024, 1)

    p_list_1, p_list_2 = get_lists("./puzzle-input.txt")
    differences = []

    p_list_1, p_list_2, differences = create_differences_list(p_list_1, p_list_2, differences)

    print(answer(differences))


if __name__ == "__main__":
    main()