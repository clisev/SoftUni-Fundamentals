deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_deck = len(deck_of_cards) // 2
    left_deck = deck_of_cards[0:middle_of_deck]
    right_deck = deck_of_cards[middle_of_deck:]
    for card_index in range(len(left_deck)):
        final_deck.append(left_deck[card_index])
        final_deck.append(right_deck[card_index])
    deck_of_cards = final_deck

print(final_deck)