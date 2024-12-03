with open("input.txt", "r") as file:
    content = file.read()

reports = content.splitlines()

total_safety = 0
for report in reports:
    safety = "safe"
    levels = report.split()
    levels = [int(level) for level in levels]
    
    if levels[0] < levels[1]:
        order = "ascending"
    elif levels[0] > levels[1]:
        order = "descending"

    for x in range(len(levels) - 1): 
        difference = abs(levels[x] - levels[x+1])
        if difference > 3 or difference < 1:
            safety="unsafe"
        
        if order == "ascending" and levels[x] > levels[x+1]:
            safety="unsafe"
        elif order == "descending" and levels[x] < levels[x+1]:
            safety="unsafe"

    if safety == "safe":
        total_safety+=1

print(total_safety)

