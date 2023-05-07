import os 
import json 

path = "/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air"
_annotations = open('annotations.json')
_train_test_set = open('training_test_set.json')

annotations_json = json.load(_annotations)
training_test_set_json = json.load(_train_test_set)

annotations = annotations_json['annotations']
categories = annotations_json['categories']


filtered_annotations = [a for a in annotations if a['image_name'] in training_test_set_json['test_set']]
for i in range(0, len(filtered_annotations)): 
    image_name = filtered_annotations[i]['image_name'].split('.')[0]
    file_content = ''
    for bounding_box in filtered_annotations[i]['bbox']:
        top = bounding_box['top']
        left = bounding_box['left']
        bottom = top + bounding_box['height']
        right = left + bounding_box['width']
        class_name = categories[bounding_box['class']]

        line = '{} {} {} {} {}\n'.format(class_name.lower(), left, top, right, bottom)
        file_content += line
    
    path = '/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air/ground_truths/{}.txt'.format(image_name)
    with open(path, 'w') as f:
        f.write(file_content)
        


