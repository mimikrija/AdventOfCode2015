# Day 11: Corporate Policy

def increment_password(in_password):
    increment = 1
    for pos in range(len(in_password)-1, -1, -1):
        new_value = ord(in_password[pos]) + increment
        if new_value <= 122: # z or 'less'
            # no wrap around
            increment = 0
        else:
            # wrap around
            new_value = 97 # a
            increment = 1

        in_password[pos] = chr(new_value)
        if increment == 0:
            return in_password


def has_three_conseq_letters(password):
    for c in range(len(password)-2):
        if ord(password[c]) == ord(password[c+1]) - 1 == ord(password[c+2]) - 2:
            return True
    return False


def does_not_have_iol(password):
    return not any(c in password for c in 'iol')


def contains_two_pairs(password):
    previous_match = ''
    count = 0
    for one, two in zip(password, password[1:]):
        if one == two and one != previous_match:
            previous_match = one
            count += 1
        if count == 2:
            return True
    return False


def is_valid(password):
    # Passwords must include one increasing straight of at least three letters
    # Passwords may not contain the letters i, o, or l
    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz
    return has_three_conseq_letters(password) and does_not_have_iol(password) and contains_two_pairs(password)


def find_new_valid(in_password):
    new_password = list(in_password)
    while True:
        new_password = increment_password(new_password)
        if is_valid(new_password):
            return "".join(c for c in new_password)

my_input = 'hxbxwxba'

part_1 = find_new_valid(my_input)
print(f'Next valid password after {my_input} is {part_1}!')
# Next valid password after hxbxwxba is hxbxxyzz!

part_2 = find_new_valid(part_1)
print(f'Next valid password after {part_1} is {part_2}!')
# Next valid password after hxbxxyzz is hxcaabcc!
