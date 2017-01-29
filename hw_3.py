import sys
import os
import paramiko

host = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]
path = sys.argv[4]
prefix = sys.argv[5]
counts = int(sys.argv[6])
mode = int(sys.argv[7], 8)

print(host)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=name)


i = 0
while i < counts:
	fld = os.path.join(path, prefix + str(i))
	stdin, stdout, stderr = ssh.exec_command('mkdir ' + fld)
	stdin, stdout, stderr = ssh.exec_command('chmod ' + str(mode) + ' ' + fld)
	i = i + 1

print('Folders were created on host: %s' % (host))


ssh.close()
