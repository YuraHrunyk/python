import rpm
import sys


path = sys.argv[1]
rpm_file = open(path)
ts = rpm.TransactionSet()
rel = ts.hdrFromFdno(rpm_file)

print('Release.........', rel[rpm.RPMTAG_RELEASE])


rpm_file.close()