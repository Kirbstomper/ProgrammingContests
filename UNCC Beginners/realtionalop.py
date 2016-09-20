cases = int(input())

for c in range(0, cases):
    line = list(map(int,input().split()))
    if line[0] == line[1]:
        print("=")
    elif line[0] < line[1]:
        print("<")
    else:
        print(">")