total_score = 0
cards_dictionary = {}
with open("input.txt", "r") as card_lines:
    for card in card_lines.readlines():
        split = card.split(":")
        card_index = int(split[0].replace("Card ", ""))

        if card_index not in cards_dictionary.keys():
            cards_dictionary[card_index] = 1
        
        winning_numbers = [elem for elem in split[1].split("|")[0].strip().split(" ") if elem]
        guess_numbers = [elem for elem in split[1].split("|")[1].strip().split(" ") if elem]

        correct_guesses = []
        for guess in guess_numbers:
            if guess in winning_numbers:
                correct_guesses.append(guess)

        for i in range(len(correct_guesses)):
            future_index = int(card_index+int(i)+1)
            if future_index <= 202 and future_index not in cards_dictionary.keys():
                cards_dictionary[future_index] = 1

            cards_dictionary[future_index] += (1 * cards_dictionary[card_index])


print(sum(cards_dictionary.values()))
#   solution - 5920640