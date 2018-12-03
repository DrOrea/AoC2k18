# 
# 
# 
import re

def main():
    with open('DayTwoInput.txt') as file:
        lines = list(line.strip('\n') for line in file.readlines())


    # PartOne
    twoCounter = threeCounter = 0
    for line in lines:
        arrChar = set(line)

        # check for two
        for c in line:
            if line.count(c) == 2:
                twoCounter += 1
                break

         # check for three
        for c in line:
            if line.count(c) == 3:
                threeCounter += 1
                break

    print(f"Checksum : {twoCounter * threeCounter}")

    # PartTwo

if __name__ == '__main__':
    main()    