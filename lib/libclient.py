# TODO: Сделать все через словарь. Вызов методов
import json
import datetime
import logging
import logging.config
import lib.libException as libException
from sys import argv
import ipaddress
import logging
import logging.config
from functools import wraps
import argparse

LOG_ON = True

logging.config.fileConfig(fname='log_config.py')
logger = logging.getLogger('filesLogger')


##########

# TODO: Переделать что бы данные отоброжались не в виде сообщения.
def log(func):
    @wraps(func)
    def log_wrap(*args, **kwargs):
        if LOG_ON:
            logger.info(
                '{} - {}, with argument: {} \n'.format(log_wrap.__module__, log_wrap.__name__, locals().items()))
        res = func(*args, **kwargs)
        return res

    return log_wrap


# Принимаеет сообщение от сервера, смотрит на поле action, выбирает дальнейшее действие
@log
def get_data_from_socket(sock):
    server_data_buf = sock.recv(1024)
    server_data = json.loads(server_data_buf.decode())
    return server_data


# TODO: Добавить проверку типов
# Формирует presence сообщение клиента
@log
def presence_message(account_name='slava', status_msg=''):
    msg = {
        'action': 'presence',
        'time': datetime.datetime.now().timestamp(),
        'type': 'status',
        'user': {
            'account_name': str(account_name),
            'status': str(status_msg)}
    }
    msg_json = json.dumps(msg)
    buf = msg_json.encode()
    # sock.send(buf)
    return buf


# @log
# def getting_arguments():
#     server_addr = '95.217.5.66'
#     server_port = 7777
#     i = 1
#     if len(argv) == 3 or len(argv) == 5:
#         while i < len(argv):
#             if argv[i] == '-p':
#                 server_port = int(argv[i + 1])
#
#             elif argv[i] == '-a':
#                 server_addr = argv[i + 1]
#             i += 1
#             if ipaddress.ip_address(server_addr) and server_port in range(1, 65535):
#                 return server_addr, server_port
#     elif len(argv) == 1:
#         if ipaddress.ip_address(server_addr) and server_port in range(1, 65535):
#             return server_addr, server_port
#     else:
#         print('Неправельное кол-во параметров')

#TODO: Доделать
@log
def getting_arguments_new():
    client_mode = 'read'
    server_addr = '95.217.5.66'
    server_port = 7777
    parser = argparse.ArgumentParser(description='Test argument parser')
    parser.add_argument('-w', action='store_true', help='Client write chat')
    parser.add_argument('-r', action='store_true', help='Client read chat')
    arg = parser.parse_args()
    if arg.w:
        client_mode = 'write'
    return server_addr, server_port, client_mode


@log
def action_function(action, sock):
    if len(action) <= 15:
        action_dist = {
            'presence': presence_message,
            'prоbe': None,
            'msg': None,
            'quit': None,
            'authenticate': None,
            'join': None,
            'leave': None

        }
        # print()
        sock.send(action_dist[action]())
    else:
        raise libException.ActionLenght


if __name__ == '__main__':
    pass
