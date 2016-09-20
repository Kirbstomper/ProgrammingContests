output = open("out.txt","w")
cases = int(input())
for c in range(1,cases+1):
    websites = []
    hits = []
    max = -1
    for x in range(0,10):
        data = input().split()
        websites.append(data[0])
        hits.append(int(data[1]))
        if int(data[1]) > max:
            max = int(data[1])
    print("Case #" + str(c)+ ":")
    output.write("Case #" + str(c)+ ":"+"\n")

    for x in range(0,10):
        if hits[x] == max:
            print(websites[x])
            output.writelines(websites[x] +"\n")