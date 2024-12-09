import os
from textwrap import wrap

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "input09.txt")
file = os.path.join(script_dir, "test09.txt")


with open(file, "r") as f:
    input = wrap(f.read(), 2)

#print(input)

result = []

count = 0
for idx, i in enumerate(input):
    if len(i) == 2:
        if int(i[0]) > 0:
            #print(i[0])
            for x in range(int(i[0])):
                result.append(idx)
        else:
            print("file = Zero")
        if int(i[1]) > 0:
            for x in range(int(i[1])):
                result.append(".")
            #print(i[1])
        else:
            continue
            #print("space = Zero")
        #result +=  (str(idx) * int(i[0])) + ("." * int(i[1]))
        #file = i[0]
        #free = i[1]
    elif len(i) == 1:
        
        if int(i[0]) > 0:
            #print(i[0])
            for x in range(int(i[0])):
                result.append(idx)
        else:
            continue
         #  print("file = Zero")
        
        #result += str(idx) * int(i[0])
        #file = i[0]
        #free = None
    count += 1

    # print(idx, "File: ", file, " Free: ", free)


tempres1 = []
for x1 in reversed(result):
    if x1 != ".":
        tempres1.append(x1)

temp1 = []
y = 0
for x in result:
    if x != ".":
        temp1.append(x)
    else:
        temp1.append(tempres1[y])
        y += 1

temp1 = temp1[0 : len(tempres1)]

ans = 0
for idxa, a in enumerate(temp1):
    ans += idxa * int(a)

print(ans)
