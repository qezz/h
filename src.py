from subprocess import call
import os
import time

heart = """.##.##.
#..#..#
#.....#
#.....#
.#...#.
..#.#..
...#..."""

def main():
    print(heart)
    # do nothin
    mx = [list(x) for x in heart.split()]
    print(mx)

    targ = [[None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]]

    for j in range(len(mx[0])):
        for i in range(len(mx)):
            print(mx[i][j], end="")
            targ[j][i] = mx[i][j]
        print()

    print(targ)

    os.chdir("/Users/sergey-mishin/dev/python/heart/")
    f = open("./tfile", "w")

    initial_date = 1390097040 + 60 * 60 * 24
    next_date = initial_date

    for week in targ:
        for day in week:
            if day != ".":
                print([week, day])
                f.seek(0)
                f.write(str(next_date) + "\n")
                nd_str = str(next_date)
                # git commit --date="1424581440"
                call(["./script.sh", nd_str])
                #time.sleep(2)
            next_date = next_date + 60*60*24



if __name__ == "__main__":
    main()
