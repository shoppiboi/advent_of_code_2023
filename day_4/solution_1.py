total_score = 0

with open("input.txt", "r") as card_lines:
    for card in card_lines.readlines():

        split = card.split(":")[1].split("|")
        winning_numbers = [elem for elem in split[0].strip().split(" ") if elem]
        guess_numbers = [elem for elem in split[1].strip().split(" ") if elem]

        correct_guesses = []
        for guess in guess_numbers:
            if guess in winning_numbers:
                correct_guesses.append(guess)

        print(correct_guesses)

        power = -1
        if len(correct_guesses) > 0:
            power = len(correct_guesses) - 1

        if power > -1:
            total_score += pow(2, power)
            print("yoyo")

print(total_score)
#   solution - 23235        