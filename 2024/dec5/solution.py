import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "input05.txt")

with open(file, "r") as f:
    input = f.read()

# rules = input.split("\n\n")[0]
rules = [x.split("|") for x in input.split("\n\n")[0].split("\n")]
pages = [x.split(",") for x in input.split("\n\n")[1].split("\n")]


def findMiddelNumber(lofnums: int):
    return int((lofnums / 2) + 0.5)


def findNext(curr, next):
    result = False
    for rule in rules:
        c = int(rule[0])
        n = int(rule[1])
        # print(f"Curr: {curr} -> {x}, Next: {next} -> {y}")
        # print(type(curr), type(x))
        if curr == c:
            if n == next:
                result = True
                break
    return result


def findPrev(curr, prev):
    result = False
    for rule in rules:
        p = int(rule[0])
        c = int(rule[1])
        # print(f"Curr: {curr} -> {x}, Next: {next} -> {y}")
        # print(type(curr), type(x))
        if curr == c:
            if p == prev:
                result = True
                break
    return result
    # return False


total = 0
wrong = []
for page in pages:
    instructions = True
    # print(page)
    # print("Middle: ", page[findMiddelNumber(len(page) - 1)])
    for idx, p in enumerate(page):
        if instructions:
            # first one - not neede to look back
            # print(idx)
            if idx == 0:
                # print("P:", p)
                # print("Next:", page[idx + 1])
                # print("First one... ")
                instructions = findNext(int(p), int(page[idx + 1]))
                # print(instructions)
            # hvis det er den sidste skal kun checkes tilbage
            elif idx == len(page) - 1:
                # print("last one foudn... ")
                # print("P:", p)
                # print("Prev:", page[idx - 1])
                instructions = findPrev(int(p), int(page[idx - 1]))
                # print(instructions)
            else:
                # print("dont results for: ", p, "index: ", idx)
                nxt = findNext(int(p), int(page[idx + 1]))
                prv = findPrev(int(p), int(page[idx - 1]))
                # print("prev: ", prv)
                # print("next: ", nxt)
                # print("result: ", nxt and prv)
                instructions = nxt and prv
        else:
            # print("Instructions not true - break.!")
            break
    if instructions:
        total = total + int(page[findMiddelNumber(len(page) - 1)])
    else:
        wrong.append(page)
print(total)
print(len(wrong))

# print(findPrev(13, 29))

exit(0)

for x in range(len(rules)):
    #
    for rule in rules:
        search = rules[x][0]
        if rule[0] == search:
            print(rule)
    print("NEW SET!")
    # print("rules of ", x, " :", rules[x])
    # if rule[0] == rules[x]:
    #   print(rule)


# print(x.split("|"))
# print("RULES:")
# print(rules)
# print("PAGES")
# print(pages)
# print(input.split("\n\n")[0].split("\n"))
# print(input.split("\n\n")[1])

# print("Rules:", rules)
# print("Updates:", updates)


# print(findMiddelNumber(5))

exit(0)
