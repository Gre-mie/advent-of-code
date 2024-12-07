def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read().split('\n')

def orginise_data(file):
    dic = {}
    for line in file:
        data = line.split(':')
        key = int(data[0])
        dic[key] = tuple(map(lambda num: int(num), data[1].strip().split(' ')))
    return dic

def add_all(arr):
    total = 0
    for num in arr:
        total += num
    return total

def check_for(func, dic):
    new_dic = dic.copy()
    valid = []
    for test_value, values in new_dic.items():
        if func(values) == test_value:
            valid.append(test_value)
    return valid
    
def remove_valid(valid_list, dic):
    new_dic = dic.copy()
    for key in valid_list:
        del new_dic[key]
    return new_dic



def main():
    
    puzzle_file = orginise_data(get_file("./puzzle-input.txt"))
    test_file = orginise_data(get_file("./test-input.txt"))

    advent_intro(2024, 7)
    equations = puzzle_file.copy()
    valid_equations = []

#    print(f"\nequations len:      ", len(equations))
 #   print(f"valid equations len:", len(valid_equations))
  #  print()

    valid_equations = check_for(add_all, equations)
    equations = remove_valid(valid_equations, equations) 

    

    print(f"\nequations len:      ", len(equations))
    print(f"valid equations len:", len(valid_equations))
    print()
    
    print(valid_equations)
            
    answer(add_all(valid_equations))



#---------------------------------------------

#    dic = {
 #       "key-one": (1,2,3),
  #      "key-two": (4,5,6),
   #     "key-three": (7,8,9),
    #    "key-four": (10,11,12),
     #   "key-five": (13,14,15)
      #     }

#    print("keys:", list(dic))
 #   del dic["key-two"]
  #  print("keys", list(dic))

#    items = dic.items()
 #   for item in items:
  #      print(item)
   # for key, values in items:
    #    print(f"key: {key}  values: {values}")

#-------------------------------------------------------


if __name__ == "__main__":
    main()