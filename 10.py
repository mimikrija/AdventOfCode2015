# Day 10: Elves Look, Elves Say

test = '1113122113'

def say_numbers(in_string):
    digit = in_string[0]
    counter = 1
    out_string = ''

    for pos in range(1, len(in_string)):
        if in_string[pos] == digit:
            counter += 1
        else:
            out_string += str(counter) + digit
            digit = in_string[pos]
            counter = 1

    out_string += str(counter) + digit
    return out_string

def play_the_elf_game(in_string, rep):
    result_string = in_string
    for _ in range(rep):
        result_string = say_numbers(result_string)
    return result_string

part_1, part_2 = (len(play_the_elf_game(test, rounds)) for rounds in {40,50})
print(part_1, part_2) # 360154 5103798

part_2 = 5103798 # 56th sum in this list https://oeis.org/A022471/b022471.txt https://oeis.org/A022471
