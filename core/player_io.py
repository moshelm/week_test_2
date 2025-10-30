def ask_player_action() -> str:
    while True:
        user_input = input('please enter H or S').strip()
        if user_input == 'S' or user_input == 'H':
            return user_input

