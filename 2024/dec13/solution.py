import os
from operator import add

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "input13.txt")
# file = os.path.join(script_dir, "test13.txt")

with open(file, "r") as f:
    input = f.read().split("\n\n")

ans = 0
for i in input:
    ii = i.split("\n")
    # print(len(ii))
    ax = int((ii[0][12:].split("X+")[0].split(","))[0])
    ay = int((ii[0].split("Y+"))[1])
    bx = int((ii[1][12:].split("X+")[0].split(","))[0])
    by = int((ii[1].split("Y+"))[1])
    px = int(ii[2].split(",")[0].split("=")[1])
    py = int(ii[2].split(",")[1].split("=")[1])
    # print(f"Button A: X={ax}, Y={ay}")
    # print(f"Button B: X={bx}, Y={by}")
    # print(f"Prize: X={px}, Y={py}")
    # print(" ")

    calcsetax = []
    calcsetay = []
    calcsetbx = []
    calcsetby = []

    for _ in range(1, 99):
        calcsetax.append(ax * _)
        calcsetay.append(ay * _)
        calcsetbx.append(bx * _)
        calcsetby.append(by * _)

    mysum = 0
    for idx, x in enumerate(calcsetax):
        for idx1, x1 in enumerate(calcsetbx):
            if x + x1 == px:
                if calcsetay[idx] + calcsetby[idx1] == py:
                    print("X: ", x)
                    print("X1: ", x1)
                    print("SUM: ", x + x1)
                    print("idx: ", idx + 1)
                    print("idx1: ", idx1 + 1)
                    print("mysum: ", mysum)
                    newsum = ((idx + 1) * 3) + ((idx1 + 1) * 1)
                    print(newsum)

                    if mysum == 0:
                        print("Mysum is 0 now new mysum is:")
                        mysum = newsum
                        print(mysum)
                    else:
                        if newsum < mysum:
                            print(
                                f"current combo {newsum} is lower than {mysum}, changing mysum to newsum"
                            )
                            mysum = newsum

    # print("MYSUM FOR:", i)
    if mysum > 0:
        # print(ans, " + ", mysum, " = ")
        ans += mysum
    #   print(ans)
    # print(mysum)  # print(x + x1)
    else:
        print("No match... ")

    # print(calcseta[0][1] + calcsetb[1][1])

    # print(reslist)

    # resxlist = list(map(add, calcsetax, calcsetbx))
    # resylist = list(map(add, calcsetay, calcsetby))
    # print("X: ", resxlist)
    # print("Y: ", resylist)

    # print("=" * 80)
    # print(calcsetax)
    # print("=" * 80)
    # print(calcsetbx)
    # print("=" * 80)

    print("NEXT.....")

print(ans)
