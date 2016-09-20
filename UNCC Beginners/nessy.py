case = int(input())
for c in range(1,case+1):
    rowcol = list(map(int,input().split()))
    print(str((rowcol[0]//3) * (rowcol[1]//3)))

