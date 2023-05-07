import os
import random
import json

path = "/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air/images"
dir_list = os.listdir(path)

test_set_size = 2823 

random.shuffle(dir_list)
test_set = dir_list[:test_set_size]
training_set = dir_list[test_set_size:]

new_object = {
    'test_set': test_set, 
    'training_set': training_set
}
json_object = json.dumps(new_object, indent=4)
with open("training_test_set.json", "w") as outfile:
    outfile.write(json_object)

print(new_object)
