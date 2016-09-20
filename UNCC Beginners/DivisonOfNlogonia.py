lines = int(input())
while lines!=0:
    dp = list(map(int,input().split()))
    for x in range(0,lines):
        test = list(map(int,input().split()))
        plane = (dp[0] - test[0],dp[1]-test[1])
        x = plane[0]
        y = plane[1]
        if plane [1 ]== 0 or plane[0] == 0:
            print("divisa")
        else:
            if x>0 :
                if y>0:
                    print("SO")
                else:
                    print("NO")
            else:
                if y>0:
                    print("SE")
                else:
                    print("NE")
    lines = int(input())