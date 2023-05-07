import os 
import json 

_annotations = open('yolo_on_test_set.json')
annotations_json = json.load(_annotations)
annotations = annotations_json['annotations']


for image in annotations: 
    file_content = ''
    image_name = image['image_name'].split('.')[0]
    
    for bbox in image['bbox']:
        top = bbox['y1']
        left = bbox['x1']
        bottom = bbox['y2']
        right = bbox['x2']
        class_name = bbox['class']

        class_name = class_name.split(' ')[0]
        line = '{} {} {} {} {} {}\n'.format(class_name.lower(), 0.99, left, top, right, bottom)
        file_content += line

    path = '/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air/detection_results/{}.txt'.format(image_name)
    with open(path, 'w') as f:
        f.write(file_content)
    
