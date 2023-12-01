#1

#with open('input.txt') as file:
#    lines = file.readlines()
#    total = 0
#    for line in lines:
#        first = -1
#        last = -1
#        for c in line:
#            if c.isdigit():
#                if first < 0:
#                    first = ord(c) - 48
#                last = ord(c) - 48
#        print(first * 10 + last)
#        total = total + first * 10 + last
#    print(total)

#2
MATCH = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

with open('input.txt') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        first = -1
        last = -1
        current_index = 0
        first_index = - 1
        last_index = - 1

        #get the real number and keep index
        for c in line:
            if c.isdigit():
                if first < 0:
                    first = ord(c) - 48
                    first_index = current_index
                last = ord(c) - 48
                last_index = current_index
            current_index = current_index + 1
        
        #get the index of string number
        i = 1
        for n in MATCH:
            index = line.find(n)
            if(index < first_index and index > -1 or first_index == -1):
                first_index = index
                first = i
            rindex = line.rfind(n)
            if(rindex > last_index):
                last_index = rindex
                last = i
            i = i + 1
            
        print(first * 10 + last)
        total = total + first * 10 + last
    print(total)