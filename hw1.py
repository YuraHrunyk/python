import sys
import os


path = sys.argv[1]
prefix = sys.argv[2]
counts = int(sys.argv[3]) + 1
mode = int(sys.argv[4], 8)


fld = ((os.path.join(path, prefix)))

i = 1

while i < counts:
	folder = fld + str(i)
	os.mkdir(folder, mode)
	i = i + 1
