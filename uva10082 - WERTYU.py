while True:
    try:
        input_line = input()
    except EOFError:
        break

    in_str = " 1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./"
    out_str = " `1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,."

    output_list = []
    for char in input_line:
        output_list.append(out_str[in_str.index(char)])

    print("".join(output_list))