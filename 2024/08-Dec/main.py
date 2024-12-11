def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        lines = file.read().split('\n')
        return list(map(lambda line: list(line), lines))
    
def print_graph(graph):
    for line in graph:
        print("".join(line))

def get_frequencies_list(file):
    frequencies_list = []
    for line in file:
        for char in line:
            if not char == '.' and not char in frequencies_list:
                frequencies_list.append(char)
    return frequencies_list

def split_file_to_multiple_frequency_graphs(file):
    frequency_graphs = {}
    frequencies_list = get_frequencies_list(file)
    for frequency in frequencies_list:
        current_graph = []
        for line in file:
            new_line = []
            for char in line:
                if char == frequency:
                    new_line.append(char)
                else:
                    new_line.append('.')
            current_graph.append(new_line)
        frequency_graphs[frequency] = current_graph
    return frequency_graphs


def main():

    puzzle_file = get_file("./puzzle-input.txt")
    test_file = get_file("./test-input.txt")

#---------------------------------------------------        
    p_graphs = split_file_to_multiple_frequency_graphs(puzzle_file)
    t_graphs = split_file_to_multiple_frequency_graphs(test_file)

# test code
    for graph in t_graphs:
        print(f"\nfrequency: {graph}")
        print_graph(t_graphs[graph])

#------------------------------------------------------

    advent_intro(2024, 8)





if __name__ == "__main__":
    main()