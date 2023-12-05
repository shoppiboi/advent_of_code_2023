game_powers = []
with open("input.txt", "r") as input_lines:
    for line in input_lines.readlines():
        split = line.split(":")

        game_index = int(split[0].split(" ")[1])

        games = split[1].lstrip().split(";")

        game_max_values = {"red": 0, "green": 0, "blue": 0}
        for game in games:

            for colour in game.split(","):
                stripped_split = colour.lstrip().split(" ")
                
                number = int(stripped_split[0])
                colour = stripped_split[1].strip()

                if number > game_max_values[colour]:
                    game_max_values[colour] = number

        power = 1
        for value in game_max_values.values():
            power *= value

        print(power)

        game_powers.append(power)

    print(sum(game_powers))
    #   solution - 66681