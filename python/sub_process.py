import subprocess
from subprocess import Popen, PIPE
p = subprocess.Popen(['ls', '-l'], stdout=PIPE)
output = p.stdout.read()
for line in output.decode('utf-8').split('\n'):
    print(line)