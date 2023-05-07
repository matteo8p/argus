import os 
import json 

training_test_set = json.load(open('training_test_set.json'))
test_set = training_test_set['test_set']
training_set = training_test_set['training_set']

image_list = set(os.listdir('/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air/images'))
file_content = ''

for image in test_set: 
    if image in image_list: 
        file_content += image + '\n'

with open('/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air/test_set.txt', 'w') as f:
    f.write(file_content)