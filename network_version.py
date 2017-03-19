import protocol
import common
import connectfour
from connectfour import GameState

def _handle_server_responses(response: str) -> bool:

    if response == 'WINNER_RED':
        print('Red Wins!')
        return True

    elif response == 'WINNER_YELLOW':
        print('Yellow Wins!')
        return True

def _get_inputs(game_state: GameState) -> ():
    return (common.get_col(game_state), common.get_move(game_state))

def _handle_red(game_state: GameState, connection: protocol.ConnectionInfo) -> GameState:
    col, move = _get_inputs(game_state)

    if move == 'p':
        game_state = connectfour.pop(game_state, col - 1)
        protocol.send_message(connection, 'POP ' + str(col))


    elif move == 'd':
        game_state = connectfour.drop(game_state, col - 1)
        protocol.send_message(connection, 'DROP ' + str(col))

    return game_state

def _handle_yellow(game_state: GameState, connection: protocol.ConnectionInfo) -> GameState:

    response = protocol.get_response(connection)
    print(response)
    
    response_list = response.split()
    col = int(response_list[1])
                
    if response_list[0] == 'POP':
        game_state = connectfour.pop(game_state, col - 1)

    elif response_list[0] == 'DROP':
        game_state = connectfour.drop(game_state, col - 1)

    return game_state

def _gameloop() -> None:
    game_state = connectfour.new_game()
    
    connection = protocol.connect('woodhouse.ics.uci.edu', 4444)
    protocol.ready_game(connection)

    while True:
        
        common.display_game_board(game_state.board)

        if game_state.turn == connectfour.RED:
            try:
                game_state = _handle_red(game_state, connection)

            except:
                common.print_general_err()
                continue

        elif game_state.turn == connectfour.YELLOW:

            try:
                game_state = _handle_yellow(game_state, connection)

            except:
                print('The server returned an invalid move, closing connection')
                protocol.close(connection)
                break
                

        response = protocol.get_response(connection)
        if _handle_server_responses(response):
            common.display_game_board(game_state.board)
            protocol.close(connection)
            break
    

if __name__ == '__main__':
    _gameloop()
                
                
            
                
            
        

    
