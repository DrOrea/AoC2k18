import re

frequency = 0

with open('DayOneInput.txt') as file:
    line = file.readlines()
    for integer in line:
        integer = re.sub('\n$','',integer)
        integer = re.sub('\+','',integer)
        frequency += int(integer)
print(frequency)