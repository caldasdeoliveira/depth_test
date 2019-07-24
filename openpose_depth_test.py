import json
import os




directory = os.path.join('.','photos')

filename = os.path.join(directory,'annotations.json')
with open(os.path.join(filename), 'r') as f:
    data = json.load(f)
print(data)

for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
        #run openpose
        print(data[1])
