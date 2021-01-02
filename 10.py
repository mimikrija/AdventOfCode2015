# Day 10: Elves Look, Elves Say

puzzle_input = '1113122113'

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

for rounds in {40, 50}:
    solution = len(play_the_elf_game(puzzle_input,rounds))
    print(f'The length of the sequence after {rounds} rounds of the "Say numbers" game is: {solution}!')

# The length of the sequence after 40 rounds of the "Say numbers" game is: 360154!
# The length of the sequence after 50 rounds of the "Say numbers" game is: 5103798!
