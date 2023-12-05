with open("input.txt", "r") as input_lines:
    number_combinations = []
    for line in input_lines.readlines():
        first_digit = None
        last_digit = None
        for letter in line:
            try:
                integer = int(letter)
            except:
                continue

            if not first_digit:
                first_digit = integer
            else:
                last_digit = integer

        if not last_digit:
            last_digit = first_digit

        str_first_digit = str(first_digit)
        str_last_digit = str(last_digit)

        number_combinations.append(int(str_first_digit + str_last_digit))

    print(sum(number_combinations))
    #   solution - 54388