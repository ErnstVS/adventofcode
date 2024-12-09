import os
from textwrap import wrap

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "input09.txt")
# file = os.path.join(script_dir, "test09.txt")


with open(file, "r") as f:
    input = wrap(f.read(), 2)

#   print(input)

result = ""
for idx, i in enumerate(input):
    if len(i) == 2:
        result += (str(idx) * int(i[0])) + ("." * int(i[1]))
        file = i[0]
        free = i[1]
    elif len(i) == 1:
        result += str(idx) * int(i[0])
        file = i[0]
        free = None

    # print(idx, "File: ", file, " Free: ", free)


tempres = result[::-1].replace(".", "")
temp1 = ""
y = 0
for x in result:
    if x != ".":
        temp1 += x
    else:
        temp1 += tempres[y]
        y += 1

temp1 = temp1[0 : len(tempres)]

ans = 0
for idxa, a in enumerate(temp1):
    ans += idxa * int(a)

print(ans)


# print(result)
# print(tempres)
# print(temp1)

#    print(x)

# print(input)
# print(result)
