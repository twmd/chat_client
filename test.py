# import subprocess
# import multiprocessing
# # def test():
# #     a = input('Enter message: ')
# #     print(a)
# arg = r'python C:\_slava\_work\Dropbox\code\Chat\chat_client\test2.py'
#
# for _ in range (2):
#     subprocess.Popen(arg, creationflags=subprocess.CREATE_NEW_CONSOLE)
#
# # args = ["ping", "www.yahoo.com"]
# # for _ in range (5):
# #     subprocess.Popen(args, creationflags=subprocess.CREATE_NEW_CONSOLE)

import argparse

parser = argparse.ArgumentParser(description='Test argument parser')
parser.add_argument('-w', action='store_true', help='Client write chat')
parser.add_argument('-r', action='store_true', help= 'Client read chat')
arg = parser.parse_args()
print(arg.w)
print(arg.r)