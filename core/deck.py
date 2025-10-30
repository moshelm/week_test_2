import random
SUITES = ['S','H','C','D']
def build_standard_deck() -> list[dict]:
    deck = []
    suites = ['S','H','C','D']
    special_rank = ['J','K','Q','A']
    for suite in suites:
        for rank in range(2,11):
            deck.append(create_card(rank,suite))
        for special in special_rank:
            deck.append(create_card(special,suite))

    return deck

def create_card(rank,suite):
    card = {
        'rank':rank,
        'suite':suite
    }
    return card

def shuffle_by_suit(deck:list[dict],swaps:int=5000) -> list[dict]:
    length_deck = len(deck)
    for _ in range(swaps):

        index_1 = random.randint(0,length_deck-1)
        card_1 = deck[index_1]
        index_2 = random.randint(0, length_deck - 1)

        while index_1 == index_2 or not shuffle_conditions(get_suite(card_1), index_2):
            index_2 = random.randint(0,length_deck-1)
        deck[index_1] , deck[index_2] = deck[index_2], deck[index_1]
    return deck
def shuffle_conditions(suite_card, index):
    if suite_card == 'H':
        return index % 5 == 0
    elif suite_card == 'C':
        return index % 3 == 0
    elif suite_card == 'D':
        return  suite_card % 2 == 0
    elif suite_card == 'S':
        return  suite_card % 7 == 0
def get_suite(card):
    return card['suite']
