N = int(input())
for n in range(N):
    count_iter = 0
    P = input()
    reversed_P = P[: :-1]

    while P != reversed_P:
        summation = int(P) + int(reversed_P)
        P = str(summation)
        reversed_P = P[::-1]
        count_iter += 1

    print(f'{count_iter} {int(P)}')