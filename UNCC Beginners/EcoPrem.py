def burden(n):
    size = n[0]
    animals = n[1]
    envfrend = n[2]

    return( ((size/animals)*envfrend)*animals)

cases = int(input())
for x in range(0,cases):
    sum = 0
    farmers = int(input())
    for x in range(0,farmers):
        sum += (burden(list(map(int,input().split()))))
    print (int(sum))