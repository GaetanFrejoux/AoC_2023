
#def filter_integer(val):
#    return val.isnumeric()
#
#def eval(line):
#    begin_game = line.split('|')
#    hand = list(filter(filter_integer, begin_game[0].split(' ')))
#    winning_numbers = list(filter(filter_integer, begin_game[1].split(' ')))
#    hand = list(map(lambda x : int(x), hand))
#    winning_numbers = list(map(lambda x : int(x), winning_numbers))
#    hand.sort()
#    winning_numbers.sort()
#    matching = 0.5
#    for v in hand:
#        if(v in winning_numbers):
#            matching = matching * 2
#    print(matching)
#    if(matching < 1): return 0
#    return matching
#
#with open('input_4.txt') as file:
#    lines = file.readlines()
#    total = 0
#    for line in lines:
#        line = line[:-1]
#        total = total + eval(line)
#    print(total)

    

def filter_integer(val):
    return val.isnumeric()

with open('input_4.txt') as file:
    lines = file.readlines()
    l = len(lines)
    instances = [1] * l
    index = 0
    for line in lines:
        line = line[:-1]
        begin_game = line.split('|')
        hand = list(filter(filter_integer, begin_game[0].split(' ')))
        winning_numbers = list(filter(filter_integer, begin_game[1].split(' ')))
        hand = list(map(lambda x : int(x), hand))
        winning_numbers = list(map(lambda x : int(x), winning_numbers))
        hand.sort()
        winning_numbers.sort()
        matching = 0
        for v in hand:
            if(v in winning_numbers):
                print(v)
                matching = matching + 1
        for i in range(index + 1, index + matching + 1):
            if(l > i):
                instances[i] = instances[i] + instances[index]
        index = index + 1
            
    print(sum(instances))