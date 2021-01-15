total = 0
strings = 0
encoding = 0

for lines in open('./inputs/input08','r'):
    line = lines.split('\n')[0] # this is to ignore new line character from counting literals
    total += len(line)
    strings += len(eval(lines)) # eval is an inverse of repr (sort of), it interprets all the escape characters
    # print ("literal string is: ", line, ". interpreted string is: ", eval(lines))
    # print (line, " length is ", len(line), "actual length is ", len(eval(lines)))
    temp = line.replace('"','\\')
    encoding += len(repr(temp))

print ("First part solution is: ", total - strings)
# First part solution is:  1333

print ("Second part solution is: ", encoding - total)
# Second part solution is:  2046
