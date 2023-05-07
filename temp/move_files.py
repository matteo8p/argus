import os 
import json 

path = "/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air"
f = open('training_test_set.json')
training_test_set = json.load(f)

test_set = training_test_set['test_set']
counter = 1

for file_name in test_set:
    print('({}/{}): Moving image {}'.format(counter, len(test_set), file_name))
    try: 
        os.rename(path + '/images/' + file_name, path + '/images_test_set/' + file_name)
    except:
        print('Could not move image {}'.format(file_name))