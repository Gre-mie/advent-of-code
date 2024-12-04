def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_input(path):
    with open(path, 'r') as file:
        content = file.read()
    return content


def find_word(word_to_find, puzzle):
    letters = len(puzzle[0])
    rows = len(puzzle)
    directions = [(+1, +0), (+1, +1), (+0, +1), (-1, +1), (-1, +0), (-1, -1), (+0, -1), (+1, -1)]


    print(f"\nFixed function vars:\nword to find: {word_to_find}\nrows: {rows}\nletters: {letters}\ndirections:\n{directions}\n")

    current_row = 0   # move by y ... by row of letters
    current_col = 0   # move by x ... by letter
    found = ""

    print(f"mutating function vars:\ncurrent row: {current_row}\ncurrent col: {current_col}\nfound: {found}\n")

#    for x, y in directions:
 #       print(f"x: {x} y: {y}")
  #      print(f"{current_col} + {y} =",current_col + y)

    test = [] # test code
    count = 0
    search_possition = 0
    #while current_row < rows and current_col < letters:
    for direction in directions:
        x = direction[0]
        y = direction[1]
        print(f"x: {x}  y: {y}")
        test = [] # test code
        
        for j in range(rows-1):
            current_col = 0
            for i in range(letters-1):
                
                letter = puzzle[j][i]
                if letter == word_to_find[search_possition]:
                    found += letter
                    print(f"found: {found}")
                    search_possition += 1
                    if search_possition > len(word_to_find) - 1:
                        search_possition = 0
                        count += 1
                else:
                    found = ""
                    search_possition = 0




                test.append(letter) # test code

                current_col += x
            
            test.append('\n')


            

        current_row += y

    print("".join(test)) # test code
    
    return count





def main():
    
    puzzle_input = get_input("./puzzle-input.txt").split("\n")
    test_input = get_input("./test-input.txt").split("\n")
    
    advent_intro(2024, 4)
    #-----------------------------------

    #print(test_input)

    test_result = find_word("XMAS", test_input)
    print(f"\nTest result: {test_result}\n")







    #-----------------------------------




if __name__ == "__main__":
    main()