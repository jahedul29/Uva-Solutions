counter = 1
while True:
    try:
        line = input()
    except EOFError:
        break

    output_str = []
    for char in line:
        if char == '\"':
            if counter == 1:
                output_str.append("``")
                counter = 0
            else:
                output_str.append("''")
                counter = 1
        else:
            output_str.append(char)

    print("".join(output_str))