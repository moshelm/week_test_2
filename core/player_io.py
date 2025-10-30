

def ask_player_action() -> str:
    while True:
        user_input = input('please enter H or S\n').strip()
        if user_input == 'S' or user_input == 'H':
            return user_input
        print('you can only enter H or S')


def display_status(hand_player, hand_dealer):
    return f"player hand:{hand_player}\ndealer hand:{hand_dealer}"
