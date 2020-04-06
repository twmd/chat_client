import os
import subprocess


path_to_file = os.path.join(os.getcwd(), 'client.py')
client_app = 'python ' + path_to_file
subprocess.Popen(client_app + ' -w', creationflags=subprocess.CREATE_NEW_CONSOLE)
subprocess.Popen(client_app + ' -r', creationflags=subprocess.CREATE_NEW_CONSOLE)
