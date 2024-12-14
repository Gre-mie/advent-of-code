from bot import Bot

def advent_intro(year, day, part=1):
    print(f"--- Advent of Code ---\n{day} December {year} - Part {part}\n")

def answer(answer):
    print(f"ANSWER: {answer}\n")

def get_file(path):
    with open(path, 'r') as file:
        return file.read().split('\n')
    
def make_bots(file, grid_size):
    bots = []
    for line in file:
        values = line.split(' ')
        position = values[0].split(',')
        velosity = values[1].split(',')
        bots.append(Bot(position[0][2:], position[1], velosity[0][2:], velosity[1], grid_size))
    return bots