total = 0
strings = 0
countlines = 0
for lines in open('./inputs/input08','r'):
    countlines += 1
    line = lines.split('\n')[0] # this is to ignore new line character from counting literals
    total += len(line)
    strings += len(eval(lines)) # eval is an inverse of repr (sort of), it interprets all the escape characters
    # print (line, " length is ", len(line), "actual length is ", len(eval(lines)))

print ("First part solution is: ", total - strings)
# first part 1333

infile = open('./inputs/input08','r')

encoding = 0
while 1:
      
    # read by character 
    char = infile.read(1)
    if not char:
        break
          
    if char == '"' or char == '\\':
        encoding += 2
    elif char!='\n': # ignore new line!!
        encoding += 1
infile.close()

encoding += countlines*2


print("Second part solution is: ", encoding - total)