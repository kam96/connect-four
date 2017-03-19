import socket
from collections import namedtuple

#woodhouse.ics.uci.edu
#4444

ConnectionInfo = namedtuple('ConnectionInfo',
                            ['socket', 'i_stream', 'o_stream'])

def connect(host: str, port: int) -> ConnectionInfo:
    conn_socket = socket.socket()
    conn_socket.connect((host, port))

    conn_input = conn_socket.makefile('r')
    conn_output = conn_socket.makefile('w')

    return ConnectionInfo(
        socket = conn_socket,
        i_stream = conn_input,
        o_stream = conn_output)

def send_message(connection: ConnectionInfo, message: str) -> None:
    connection.o_stream.write(message + '\r\n')
    connection.o_stream.flush()

def get_response(connection: ConnectionInfo) -> str:
    return connection.i_stream.readline()[:-1]

def ready_game(connection: ConnectionInfo) -> None:
    send_message(connection, 'I32CFSP_HELLO ' + input('username '))
    print(get_response(connection))

    send_message(connection, 'AI_GAME')
    print(get_response(connection))

def close(connection: ConnectionInfo) -> None:
    connection.i_stream.close()
    connection.o_stream.close()
    connection.socket.close()
