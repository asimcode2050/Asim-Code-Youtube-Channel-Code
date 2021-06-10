import subprocess
cmd = "sudo blkid"
process = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
