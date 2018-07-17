import string

DEBUG = True
def dprint(obj):
    global DEBUG
    if DEBUG:
        print(obj)
        
def col2num(col):
    # this function by Sylvain on stack overflow
    # https://stackoverflow.com/a/12640614
    # thanks Slyvain!
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num

def num2col(n):
    # this function was written by sundar nataraj and MinChul on stack overflow
    # https://stackoverflow.com/a/23862195
    # thanks guys!
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string
def id2coord(idstr):
    dprint(idstr)
    num = ""
    col = ""
    #this is inelegant:
    try:
        while True:
            c = idstr[0]
            idstr = idstr[1:]
            if c.isdigit():
                num+=c
            else:
                idstr = c + idstr
                break
        if idstr.isalpha():
            col = idstr
        dprint(num)
        dprint(col)
        if num and col:
            return (int(num)-1, col2num(col)-1)
        else:
            return False
    except:
        dprint("something went wrong?")
        return False

# 0-indexed internally:
data = []
outstr = ""
with open("input.csv") as input:
    text = input.read()
    for index, line in enumerate(text.splitlines(), start=1):
        data.append(line.split(","))

with open("transform.csv") as input:
  text = input.read()
  for index, line in enumerate(text.splitlines(), start=1):
        for item in line.split(","):
            coord = id2coord(item)
            if coord:
                outstr+=str(data[coord[0]][coord[1]])
            else:
                outstr+=str(item)
            outstr+=","
        outstr+="\n"
with open("output.csv", "w") as output:
    dprint(data)
    dprint(outstr)
    output.write(outstr)            
