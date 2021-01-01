# Day 10: Elves Look, Elves Say

test = '1113122113'

def count_conseq(in_string):
    if len(in_string) == 1:
        return 1, in_string
    counter = 1
    for c, p in zip(in_string, in_string[1:]):
        digit = c
        if c == p:
            counter += 1
        else:
            return counter, digit
    return counter, digit

def elves_say(in_string):
    pos = 0
    out_string = ''
    while pos < len(in_string):
        counter, digit = count_conseq(in_string[pos:])
        pos += counter
        out_string += str(counter) + digit
    return out_string

def play_the_elf_game(in_string, rep):
    result_string = in_string
    for _ in range(rep):
        result_string = elves_say(result_string)
    return result_string

print(play_the_elf_game('3',5) == test)
print(len(play_the_elf_game(test,40)))    # 360154 (this is actually the 46th member of a sequence started by 3)

part_2 = 5103798 # 56th sum in this list https://oeis.org/A022471/b022471.txt https://oeis.org/A022471
