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



def main():
    
    puzzle_file = orginise_data(get_file("./puzzle-input.txt"))
    test_file = orginise_data(get_file("./test-input.txt"))

    print(test_file, "\n")

    advent_intro(2024, 7)


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