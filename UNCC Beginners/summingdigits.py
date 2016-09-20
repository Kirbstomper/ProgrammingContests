def g(n):
    numbers = list(map(int, list(n)))

    s = sum(numbers)
    if len(str(s))>1:
        g(str(s))
    else:
        print(str(s))

num = input()
while (num!="0"):
    g(num)
    num = input()