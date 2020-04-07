import socket
import lib.libclient as libclient


def start_client():
    # Получить адресс и порт из функции
    address, port, client_mode = libclient.getting_arguments_new()
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    client_socket.connect((address, port))
    # Отсылает в функцию что должно уйти сообщение presence
    # libclient.action_function('presence', client_socket)

    # Тест. Выводит ответ сервера в консоль
    # print(libclient.get_data_from_socket(client_socket))
    # client_socket.close()
    if client_mode == 'write':
        while True:
            libclient.send_message_in_chat(client_socket)

    elif client_mode == 'read':
        while True:
            data = client_socket.recv(1024)
            print(data)
            data = libclient.get_data_from_socket(client_socket)
            print(data)
            if data.get('action') == 'msg':
                print(data.get('message'))


if __name__ == '__main__':
    start_client()
