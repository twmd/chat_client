import socket
import lib.libclient as libclient
import select

def start_client():
    # Получить адресс и порт из функции
    address, port, client_mode = libclient.getting_arguments_new()
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    client_socket.connect((address, port))
    client_in = [client_socket]
    if client_mode == 'write':
        while True:
            libclient.send_message_in_chat(client_socket)

    elif client_mode == 'read':

        libclient.presence_message(client_socket)
        while True:
            soc_client_r, _, _ = select.select(client_in, [], [], 1)
            for s in soc_client_r:
                try:
                    data = libclient.get_data_from_socket(client_socket)
                    if data.get('action') == 'msg' and data.get('message'):
                        print(data.get('message'))
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    start_client()
