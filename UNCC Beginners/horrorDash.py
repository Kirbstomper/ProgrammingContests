cases = int(input())
for c in range(1,cases+1):
    speed = -1
    crea = list(map(int, input().split()))
    for x in crea:
        if x > speed:
            speed = x
    print("Case " + str(c)+ ": "+str(speed))
