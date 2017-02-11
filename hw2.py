from glob import glob
import json
import sys


path_to_files = sys.argv[1]
path_to_result = sys.argv[2]


import_files = glob(path_to_files + '*.json')


res_dict = {}
current_numb = 0


for file in import_files:
    fp = open(file)
    result_file = json.load(fp)
    if float(result_file['number']) > current_numb and result_file['result'] != 0:
        res_dict["id"] = result_file['id']
        res_dict["number"] = result_file['number']
        res_dict["committer_name"] = result_file['committer_name']
        res_dict["committer_email"] = result_file['committer_email']
        current_numb = int(result_file['number'])


with open(path_to_result, 'w') as outfile:
    json.dump(res_dict, outfile)


