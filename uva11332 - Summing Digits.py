while True:
    integer = input()
    if int(integer) == 0:
        break

    while len(integer) != 1:
        sum_integer = 0
        for char in integer:
            sum_integer += int(char)
        integer = str(sum_integer)

    print(int(integer))