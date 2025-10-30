from player_io import ask_player_action
def calculate_hand_value(hand:list[dict]) -> int:
    sum_hand = 0
    for card in hand:
        sum_hand += get_rank_value(card['rank'])
    return sum_hand

def get_rank_value(rank:str):
    if not rank.isdigit():
        if rank == 'A':
            return 1
        return 10
    else:
        return int(rank)
def deal_two_each(deck:list[dict], player:dict, dealer:dict) -> None :
    for _ in range(2):
        dealer['hand'].append(deck.pop(0))
        player['hand'].append(deck.pop(0))
    print(f"dealer hand:{calculate_hand_value(dealer['hand'])}\nplayer hand:{calculate_hand_value(player['hand'])}")

def dealer_play(deck:list[dict], dealer:dict) -> bool:
    value_hand = calculate_hand_value(dealer['hand'])
    while value_hand < 17:
        get_card(deck,dealer['hand'])
        value_hand = calculate_hand_value(dealer['hand'])
    if value_hand > 21:
        print('you fail')
        return False
    else:
        return True
def check_state(value_hand):
    if value_hand > 21:
        print('you fail')
        return False
    return True
def get_card(deck,hand):
    if deck:
        hand.append(deck.pop(0))

def run_full_game(deck:list[dict], player:dict, dealer:dict) -> None :
    deal_two_each(deck,player,dealer)
    while True:
        player_action = ask_player_action()
        if player_action == 'H':
            get_card(deck,player['hand'])
            hand_value = calculate_hand_value(player['hand'])
            if hand_value > 21:
                print('losser')
                return
        elif player_action == 'S':
             if dealer_play(deck, dealer):
                 value_hand_player =calculate_hand_value(player['hand'])
                 value_hand_dealer =calculate_hand_value(dealer['hand'])
                 if value_hand_player > value_hand_dealer:
                     print('you winn')
                 elif value_hand_dealer > value_hand_player:
                     print('house always winning')
                 else:
                     print('draw')
                 print(f"player with:{value_hand_player}\ndealer with:{value_hand_dealer}")


