T = int(input())
for t in range(T):
    input_list = input().split()
    input_list = map(int, input_list)
    input_list = list(input_list)
    input_list.sort()
    print(f'Case {t+1}: {input_list[-1]}')