from sys import stdin

while True:
    n, m = map(int, stdin.readline().split())
    if n == 0 and m == 0:
        break

    hl = sorted([int(stdin.readline()) for i in range(n)], reverse=True)
    kl = sorted([int(stdin.readline()) for i in range(m)], reverse=True)

    doomed = True
    c = 0

    while len(kl) >= len(hl):
        knight = kl.pop()
        if knight >= hl[-1]:
            hl.pop()
            c += knight

        if len(hl) == 0:
            doomed = False
            break

    if doomed:
        print("Loowater is doomed!")
    else:
        print(c)
