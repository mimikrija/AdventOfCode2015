# Day 11: Corporate Policy

inc_letter = lambda c: 97 if c == 122 else c + 1

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
    return all(c not in password for c in 'iol')

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

my_input = list('hxbxwxba')

new_password = list(my_input)

while not is_valid(new_password):
    new_password = increment_password(new_password)

print("".join(c for c in new_password)) # not hxcaabcc