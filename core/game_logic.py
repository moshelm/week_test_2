from core.player_io import ask_player_action,display_status


def calculate_hand_value(hand:list[dict]) -> int:
    sum_hand = 0
    for card in hand:
        sum_hand += get_card_value(card)
    return sum_hand

def get_card_value(card:dict) -> int:
    rank = card['rank']
    if not rank.isdigit():
        # value for 'A' is 1
        if rank == 'A':
            return 1
        # value for special cards is 10
        return 10
    else:
        # value of normal card
        return int(rank)


def deal_two_each(deck:list[dict], player:dict, dealer:dict) -> None :
    player_hand = player['hand']
    dealer_hand = dealer['hand']
    # dealing two cards
    for _ in range(2):
        get_card(deck,player_hand)
        get_card(deck,dealer_hand)
    hand_player_value = calculate_hand_value(player_hand)
    hand_dealer_value = calculate_hand_value(dealer_hand)
    print(f"start with \n{display_status(hand_player_value, hand_dealer_value)}")

def dealer_play(deck:list[dict], dealer:dict) -> bool:
    dealer_hand = dealer['hand']
    value_hand = calculate_hand_value(dealer_hand)
    while value_hand < 17:
        get_card(deck,dealer_hand)
        value_hand = calculate_hand_value(dealer_hand)
    if value_hand > 21:
        print('you winn. house over 21')
        return False
    else:
        return True


def get_card(deck:list[dict], hand:list[dict]) :
    # check if deck empty
    if deck:
        hand.append(deck.pop(0))
    else:
        raise 'deck is finish'

def run_full_game(deck:list[dict], player:dict, dealer:dict) -> None :
    player_hand = player['hand']
    dealer_hand = dealer['hand']

    print('game start')
    # dealing cards
    deal_two_each(deck,player,dealer)


    while True:
        player_action = ask_player_action()
        # player wants HIT
        if player_action == 'H':
            # adding cards
            get_card(deck,player_hand)
            # calculate hand
            hand_value = calculate_hand_value(player_hand)
            print(hand_value)
            if hand_value > 21:
                print('losser')
                print(display_status(hand_value, calculate_hand_value(dealer_hand)))
                return
        #     player wants STAND
        elif player_action == 'S':
             if dealer_play(deck, dealer):
                 # calculate hands
                 value_hand_player =calculate_hand_value(player_hand)
                 value_hand_dealer =calculate_hand_value(dealer_hand)
                 if value_hand_player > value_hand_dealer:
                     print('you winn')
                 elif value_hand_dealer > value_hand_player:
                     print('house always winning')
                 else:
                     print('draw')
                 print(display_status(value_hand_player,value_hand_dealer))
             return

