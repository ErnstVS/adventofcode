import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "input04.txt")

with open(file, "r") as f:
    input = f.read().split()

matrix = []

# lav matrix ud fra input filen
for line in input:
    temp = []
    for char in line:
        temp.append(char)
    matrix.append(temp)

wx = len(matrix[0])  # få bredden af matrix
ly = len(matrix)  # få længden af matrix


# print("bredde:", wx)
# print("højde:", ly)

xstart = []

dirvec = [
    [
        (
            -1,
            -1,
        ),
        (-2, -2),
        (-3, -3),
    ],
    [(0, -1), (0, -2), (0, -3)],
    [(1, -1), (2, -2), (3, -3)],
    [(-1, 0), (-2, 0), (-3, 0)],
    [(1, 0), (2, 0), (3, 0)],
    [(1, 1), (2, 2), (3, 3)],
    [(0, 1), (0, 2), (0, 3)],
    [(-1, 1), (-2, 2), (-3, 3)],
]

# for x in range(10):
#    for dir in dirvec:
#        for pair in dir:
#            print(pair[0], pair[1])


def checkword(word):
    temp = ""
    for x in range(wx):
        for y in range(ly):
            # find all occurences of X and add to list of tuples (coordinates)
            # print(x, y)
            if matrix[x][y] == word[0]:
                # add the coordinates to a list of tuples
                mytuple = (x, y)
                xstart.append(mytuple)
                # print(f"x,y:{x},{y}")

    result = 0
    # print(type(xstart))
    # print(xstart)
    for coord in xstart:
        start_x = coord[0]
        start_y = coord[1]
        print("=" * 80)
        print("start:", start_x, start_y)
        print("=" * 80)
        for dir in dirvec:
            print("new direction")
            # getting the first letter of the word
            temp = matrix[start_x][start_y]
            print(temp)
            colist = []
            colist.append(coord)
            # print("show the direction of the list->: ")
            # print(dir)
            for pair in dir:
                print(pair)
                newx = start_x + pair[0]
                newy = start_y + pair[1]
                print(f"newx {newx} and newy: {newy}")

                if newx >= 0 and newx < wx and newy >= 0 and newy < ly:
                    # temp = temp  # + matrix[coord0][0]
                    temp = temp + matrix[newx][newy]
                    #                print("=" * 80)
                    #                print(temp)
                    #                print("=" * 80)
                    pair1 = (coord[0] + pair[0], coord[1] + pair[1])
                    # print(pair1)
                    colist.append(pair1)
                else:
                    print("out of range")
                    break
                    # continue
            print(temp)

            if temp == word:
                result += 1
                # print("MATCH!!!")
                # print("=" * 80)
                print(colist)
        # run thrugh the list and check all posibilities:
        #
        #       (x-1,y-1)   (x, y-1)    (x+1,y-1)
        #       (x-1,y)        X        (x+1,y)
        #       (x-1, y+1)  (x, y+1)    (x+1,y+1)

    #    result = xstart
    return result


# checkword("XMAS")
print(checkword("XMAS"))


# print(x, y)
# print(matrix[0][5])
