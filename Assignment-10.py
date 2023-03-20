import re

fname = input("Enter a file:")
try:
    handle = open(fname)
except:
    print("Error, invalid input")
    quit()

sum = 0
for line in handle:
    line = line.rstrip()
    if len(line) != 0:
        num = re.findall('[0-9]+', line)
        for n in num:
            n = int(n)
            sum = sum + n
            
print("Sum =", sum)