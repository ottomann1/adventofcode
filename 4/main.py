with open("input.txt", "r") as file:
    content = file.read()

reports = content.splitlines()

total_safety = 0
def safetychecker(levels):
    safety = "safe"
    print(levels)


    for x in range(len(levels) - 1): 
        difference = abs(levels[x] - levels[x+1])
        if difference > 3 or difference < 1:
            safety="unsafe"
            return safety

        if levels[x] < levels[x+1]:
            order = "ascending"
        elif levels[x] > levels[x+1]:
            order = "descending"
        
        if order == "ascending" and levels[x] > levels[x+1]:
            safety="unsafe"
            return safety
        elif order == "descending" and levels[x] < levels[x+1]:
            safety="unsafe"
            return safety
    return safety

for report in reports:
    levels = report.split()
    levels = [int(level) for level in levels]
    
    safety = safetychecker(levels)

    if safety == "unsafe":
        for x in range(len(levels) - 1, -1, -1):
            oldlevels = levels[:]
            levels.pop(x)
            safety = safetychecker(levels)
            if safety == "safe":
                break
            levels = oldlevels
            

    if safety == "safe":
        total_safety+=1

print(total_safety)


