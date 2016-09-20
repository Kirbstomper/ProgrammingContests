def decode(n):
    if int(n) in [1,4,78]:
        print("+")
    elif (n[len(n)-2]+n[len(n)-1]) == "35":
        print("-")
    elif(n[0]=="9" and n[len(n)-1]=="4"):
        print("*")
    elif(n[0]+n[1]+n[2] == "190"):
        print("?")

cases = int(input())
for c in range(0,cases):
    decode(input())
