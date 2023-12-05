import re

word_to_digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("input.txt", "r") as input_lines:
    number_combinations = []
    for line in input_lines.readlines():
        first_digit = None
        first_digit_index = -1
        last_digit = None
        last_digit_index = -1

        for i, letter in enumerate(line):
            try:
                integer = int(letter)
            except:
                continue

            if not first_digit:
                first_digit = integer
                first_digit_index = i
            else:
                last_digit = integer
                last_digit_index = i

        if not last_digit and first_digit:
            last_digit = first_digit
            last_digit_index = first_digit_index

        first_digit_index = first_digit_index if first_digit_index > -1 else 0
        last_digit_index = last_digit_index if last_digit_index > -1 else 0

        for key in word_to_digit_map.keys():

            found_instances = [m.start() for m in re.finditer(key, line)]
            
            if  len(found_instances) <= 0:
                continue

            min_position = min(found_instances)
            max_position = max(found_instances)

            if min_position <= first_digit_index:
                first_digit = word_to_digit_map[key]
                first_digit_index = min_position

            if max_position >= last_digit_index:
                last_digit = word_to_digit_map[key]
                last_digit_index = max_position

        number_combinations.append(int(str(first_digit)+str(last_digit)))

    print(sum(number_combinations))