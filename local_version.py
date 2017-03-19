import connectfour
from connectfour import GameState
import common

def _get_inputs(game_state: GameState) -> ():
    return (common.get_col(game_state) - 1, common.get_move(game_state))

def _handle_inputs(game_state: GameState) -> GameState:
    col, move = _get_inputs(game_state)

    try:
        if move == 'p':
            return connectfour.pop(game_state, col)

        elif move == 'd':
            return connectfour.drop(game_state, col)

    except:
        common.print_general_err()
        return _handle_inputs(game_state)

def _main() -> None:
    game_state = connectfour.new_game()

    while True:
        common.display_game_board(game_state.board)
        game_state = _handle_inputs(game_state)

        winner = connectfour.winner(game_state)
        if winner == connectfour.RED:
            common.display_game_board(game_state.board)
            print('Red Wins!')
            break

        elif winner == connectfour.YELLOW:
            common.display_game_board(game_state.board)
            print('Yellow Wins!')
            break

if __name__ == '__main__':
    _main()
