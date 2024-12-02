def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

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

def answer_part1(differences):
    total = add(differences)
    return total

def create_differences_list(list_1, list_2, differences):
    l1 = list_1.copy()
    l2 = list_2.copy()
    for _ in range(len(list_1)):
        smallest_in_list_1 = min(l1)
        smallest_in_list_2 = min(l2)
        differences.append(find_difference(smallest_in_list_1, smallest_in_list_2))
        l1.remove(smallest_in_list_1)
        l2.remove(smallest_in_list_2)
    return differences

def count_duplicates(num_to_find, list_to_search):
        count = 0
        for item in list_to_search:
            if item == num_to_find:
                count += 1
        return count


def main():
    advent_intro(2024, 1)

    puzzle_list_1, puzzle_list_2 = get_lists("./puzzle-input.txt")
    differences = []

    differences = create_differences_list(puzzle_list_1, puzzle_list_2, differences)

    answer(answer_part1(differences))
    
    advent_intro(2024, 1, 2)

    simularities_score = 0
    for item in puzzle_list_1:
        simularities_score += item * count_duplicates(item, puzzle_list_2)
    
    answer(simularities_score)


if __name__ == "__main__":
    main()