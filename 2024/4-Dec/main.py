def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_input(path):
    with open(path, 'r') as file:
        content = file.read()
    return content

def find_word(word_to_find, puzzle):
    row_len = len(puzzle[0])
    col_len = len(puzzle)

    print(f"function vars:\nword to find: {word_to_find}\nrow len: {row_len}\ncol len: {col_len}\n")





def main():
    
    puzzle_input = get_input("./puzzle-input.txt").split("\n")
    test_input = get_input("./test-input.txt").split("\n")
    
    advent_intro(2024, 4)
    #-----------------------------------

    print(test_input)

    test_result = find_word("XMAS", test_input)
    print(f"\nTest result: {test_result}\n")







    #-----------------------------------




if __name__ == "__main__":
    main()