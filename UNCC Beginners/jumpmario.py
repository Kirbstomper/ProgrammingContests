cases = int(input())
for x in range(1,cases+1):
    pillars = int(input())
    heights = input().split()
    heights = list(map(int, heights))

    hiJump = 0
    lowJump = 0

    if pillars>1:
        for p in range(0,pillars-1):
            if heights[p]<heights[p+1]:
                hiJump+=1
            if heights[p]>heights[p+1]:
                lowJump+=1
    print("Case "+ str(x) + ": "+ str(hiJump) + " " + str(lowJump))




