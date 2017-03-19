#KB
import connectfour
from connectfour import GameState

def _player_id_to_str(player_id: int) -> str:
    if player_id == connectfour.RED:
        return 'Red'
    elif player_id == connectfour.YELLOW:
        return 'Yellow'

    else:
        return ''

def _board_value_to_str(value: int) -> str:
    if value == connectfour.RED:
        return 'R'

    elif value == connectfour.YELLOW:
        return 'Y'

    else:
        return '.'

def display_game_board(board: [[int]]) -> None:
    title_line = range(1, connectfour.BOARD_COLUMNS + 1)
    title_line = [str(i) for i in title_line]
    print(' '.join(title_line))

    row_index = 0
    while row_index < connectfour.BOARD_ROWS:
        list_to_print = []
        
        for col in board:
            list_to_print.append(col[row_index])

        list_to_print = [_board_value_to_str(i) for i in list_to_print]        
        print(' '.join(list_to_print))
        
        row_index += 1

def get_col(game_state: GameState) -> int:
    player = _player_id_to_str(game_state.turn)
    user_input = input(player + ' turn. Select a column ')
    try:
        return int(user_input)

    except:
        print_general_err()
        return get_col(game_state)
    
def get_move(game_state: GameState) -> str:
    user_input = input("P(Pop) or D(Drop) ").lower()

    if user_input == 'p' or user_input == 'd':
        return user_input

    else:
        print_general_err()
        return get_move(game_state)

def print_general_err() -> None:
    print('Invalid Move')
