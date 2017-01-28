import sys, os

path = sys.argv[1]
prefix = sys.argv[2]
counts = int(sys.argv[3])
mode = int(sys.argv[4], 8)


fld = ((os.path.join(path, prefix)))

for i in range (1, counts+1):
	folder = fld + str(i)
	os.mkdir(folder, mode)
