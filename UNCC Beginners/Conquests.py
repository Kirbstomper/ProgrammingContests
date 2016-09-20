from collections import OrderedDict
lines = int(input())
countries = {}
for x in range(0, lines):
    con = list(input().split())
    c = str(con[0])
    if countries[c] is None:
        countries[c] = 1
    else:
        countries[c] += 1

for x in countries:
    print(x)
