import hashlib

def is_solution(input, number, zeroes):
    candidate = input + str(number)
    result = hashlib.md5(candidate.encode())
    if result.hexdigest()[0:zeroes] == zeroes*"0":
        return True
    else:
        return False


my_input = "ckczppom"
solution = 1

while not is_solution(my_input,solution,5):
    solution += 1

print ("First part solution is: ", solution)
# First part solution is:  117946

while not is_solution(my_input,solution,6):
    solution += 1

print ("Second part solution is: ", solution)
# Second part solution is:  3938038
