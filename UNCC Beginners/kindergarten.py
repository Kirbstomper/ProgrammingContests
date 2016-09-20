import sys

try:
    lines = sys.stdin.read()
    count = 0
    for l in lines:
        for x in l.split():
            if x.lower().islower():
                count+=1
        print(count)
except EOFError:
    print("shit")
