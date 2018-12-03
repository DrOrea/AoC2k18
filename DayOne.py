# 
# 
# 

def main():
    # FileReading
    with open('DayOneInput.txt') as file:
        lines = list(map(int, file.readlines()))

    # PartOne
    frequency = sum(lines)
    print(frequency)

    # PartTwo
    frequency = 0
    array = set([0])

    while True:
        for line in lines:
            frequency += line
            if frequency in array:
                print(frequency)
                return
            array.add(frequency)

if __name__ == '__main__':
    main()