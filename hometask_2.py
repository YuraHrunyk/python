import glob, json, sys

path_in = sys.argv[1]
path_out = sys.argv[2]

rs = {}
ver = 0



import_files = glob.glob(path_in+'*.json')


for file in import_files:
    fp = open(file)
    res_file = json.load(fp)
    if float(res_file['number']) > ver and res_file['result'] != 0:
        rs["id"] = res_file['id']
        rs["number"] = res_file['number']
        rs["committer_name"] = res_file['committer_name']
        rs["committer_email"] = res_file['committer_email']
        ver = int(res_file['number'])


with open(path_out, 'w') as outfile:
    json.dump(rs, outfile)


