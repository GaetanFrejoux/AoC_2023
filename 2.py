#1
#
#MATCH = [ "red", "green", "blue" ]
#MAX = [12, 13, 14]
#
#def possible(line):
#    begin_game = line.split(':')
#    value = int(begin_game[0].split(' ')[1])
#    rounds = begin_game[1].split(';')
#
#    for round in rounds:
#        items = round.split(',')
#        for item in items:
#            value_color = item.split(' ')
#            if(MAX[MATCH.index(value_color[2].replace("\n", ""))] < int(value_color[1])):
#                print(value)
#                print('impossible')
#                return 0
#    return value
#
#with open('input.txt') as file:
#    lines = file.readlines()
#    total = 0
#    for line in lines:
#        total = total + possible(line)
#        print(total)
#    print(total)


#2

MATCH = [ "red", "green", "blue" ]

def eval(line):
    begin_game = line.split(':')
    rounds = begin_game[1].split(';')
    MAX = [0, 0, 0]
    for round in rounds:
        items = round.split(',')
        for item in items:
            value_color = item.split(' ')
            color_index = MATCH.index(value_color[2].replace("\n", ""))
            if(MAX[color_index] < int(value_color[1])):
                MAX[color_index] = int(value_color[1])
    return MAX[0] * MAX[1] * MAX[2]

with open('input.txt') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        total = total + eval(line)
    print(total)