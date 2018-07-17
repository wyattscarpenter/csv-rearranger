import string

DEBUG = False
def dprint(obj):
    global DEBUG
    if DEBUG:
        print(obj)
        
def col2num(col):
    # this function by Sylvain on stack overflow, thanks Slyvain!
    # https://stackoverflow.com/a/12640614
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num

def id2coord(idstr):
    dprint(idstr)
    num = ""
    col = ""
    #this is a bit inelegant:
    while idstr: # pull out the digits
        c = idstr[0]
        idstr = idstr[1:]
        if c.isdigit():
            num+=c
        else:
            idstr = c + idstr
            break
    if idstr.isalpha(): #check if the remaining portion is valid for an id
        col = idstr
    dprint(num)
    dprint(col)
    if num and col:
        return (int(num)-1, col2num(col)-1)
    else:
        return False

data = [] # 0-indexed internally
outstr = ""

with open("input.csv") as input:
    text = input.read()
    for line in text.splitlines():
        data.append(line.split(","))

with open("transform.csv") as transform:
  text = transform.read()
  for line in text.splitlines():
        for item in line.split(","):
            item = item.strip() # in case the user put in erronious spaces
            if item == "":
                break
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
