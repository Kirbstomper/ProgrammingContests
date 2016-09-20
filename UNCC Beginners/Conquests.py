from collections import OrderedDict
lines = int(input())
countries = OrderedDict()
for x in range(0, lines):
    con = list(input().split())
    c = str(con[0])
    if c in countries:
        countries[c] += 1
    else:
        countries[c] = 1
#        countries[c] += 1

for x in sorted(countries.keys()):
    print(x + " " + str(countries[x]))
