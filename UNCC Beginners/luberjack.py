cases = int(input())
print("Lumberjacks:")
for x in range(0,cases):
    line = list(map(int, input().split()));
    sortedLine = sorted(line)

    if sortedLine == line:
        print("Ordered")

    else:
        sortedLine.sort(reverse=True)
        if sortedLine == line:
            print("Ordered")
        else:
            print("Unordered")
