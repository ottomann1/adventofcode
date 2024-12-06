import re

with open("input.txt", "r") as file:
    content = file.read()

pattern = r'mul\((\d+),(\d+)\)'

all_muls = re.findall(pattern, content)

total = 0

for mul in all_muls:
    total += int(mul[0])*int(mul[1]) 

print(total)