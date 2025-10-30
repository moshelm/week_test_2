import random


def build_standard_deck() -> list[dict]:
    deck = []
    suites = ['S','H','C','D']
    special_rank = ['J','K','Q','A']
    for suite in suites:

        # adding normal cards
        for rank in range(2,11):
            card = create_card(str(rank),suite)
            deck.append(card)

        # adding special cards
        for special in special_rank:
            card = create_card(special,suite)
            deck.append(card)

    return deck


def create_card(rank:str, suite:str) -> dict:
    card = {
        'rank':rank,
        'suite':suite
    }
    return card

def shuffle_by_suit(deck:list[dict], swaps:int = 5000) -> list[dict]:
    length_deck = len(deck)

    for _ in range(swaps):
        index_1 = random.randint(0,length_deck-1)
        card_1 = deck[index_1]

        index_2 = random.randint(0, length_deck - 1)
        suite_card_1 = get_suite(card_1)

        while index_1 == index_2 or not shuffle_conditions(suite_card_1, index_2):
            # Does not meet the conditions, changing card
            index_2 = random.randint(0,length_deck-1)
        # swaps cards
        deck[index_1] , deck[index_2] = deck[index_2], deck[index_1]

    return deck


def shuffle_conditions(suite_card:str, index:int):
    if suite_card == 'H':
        return index % 5 == 0
    elif suite_card == 'C':
        return index % 3 == 0
    elif suite_card == 'D':
        return  index % 2 == 0
    elif suite_card == 'S':
        return  index % 7 == 0


def get_suite(card:dict) -> str:
    return card['suite']
