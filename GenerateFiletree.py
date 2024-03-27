import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d


f = open("./filetree.json", "w")
f.write(json.dumps(path_to_dict('Content/')))
f.close()


print(json.dumps(path_to_dict('Content/')))