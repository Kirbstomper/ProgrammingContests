cases = int(input())
for c in range(1,cases+1):
    salaries = list(map(int,input().split()))
    salaries.sort()
    print("Case " + str(c)+ ": "+str(salaries[1]))