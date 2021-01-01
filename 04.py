import hashlib

has_n_leading_zeroes = lambda code, n: all(c == '0' for c in code[:n])

def lowest_positive(in_code, leading_zeroes):
    number = 0
    found = False
    while not found:
        number += 1
        candidate = in_code + str(number)
        hash_code = hashlib.md5(candidate.encode()).hexdigest()
        found = has_n_leading_zeroes(hash_code, leading_zeroes)
    return number


my_input = "ckczppom"

part_1 = lowest_positive(my_input, 5)
print ("First part solution is: ", part_1)
# First part solution is:  117946

part_2 = lowest_positive(my_input, 6)
print ("Second part solution is: ", part_2)
# Second part solution is:  3938038
