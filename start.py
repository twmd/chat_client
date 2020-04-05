import os
import subprocess


path_to_file = os.path.join(os.getcwd(), 'client.py')
client_app = 'python ' + path_to_file
print(client_app)
subprocess.Popen(client_app, creationflags=subprocess.CREATE_NEW_CONSOLE)
