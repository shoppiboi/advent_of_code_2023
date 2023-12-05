
absolute_max_values = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_sum = 0
valid_games = []
valid_game_powers = []

with open("input.txt", "r") as input_lines:
    for line in input_lines.readlines():
        split = line.split(":")

        game_index = int(split[0].split(" ")[1])
        print(game_index)

        games = split[1].lstrip().split(";")

        game_max_values = {"red": 0, "green": 0, "blue": 0}
        for game in games:

            for colour in game.split(","):
                stripped_split = colour.lstrip().split(" ")
                
                number = int(stripped_split[0])
                colour = stripped_split[1].strip()

                if number > game_max_values[colour]:
                    game_max_values[colour] = number

        valid = True
        for key in game_max_values.keys():
            if game_max_values[key] > absolute_max_values[key]:
                valid = False
        
        if valid:
            valid_games.append(game_index)

    print(sum(valid_games))
    #   solution - 2237