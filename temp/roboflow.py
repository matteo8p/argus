import os 
import json 

f = open('annotations.json')
annotations = json.load(f)['annotations']

image_path = '/Users/matt8p/Desktop/School Stuff/Spring 2023/argus/au-air/images_test_set'
image_names = filter(lambda p: '.jpg' in p, os.listdir(image_path))

for image in image_names: 
    image_information = filter(lambda p: p['image_name'] == image, annotations)[0]
    image_width = 1920.0
    image_height = 1080.0
    file_content = ''

    for img_object in image_information['bbox']:
        y_center_normalized = (2 * img_object['top'] + img_object['height']) / 2 / image_height
        x_center_normalized = (2 * img_object['left'] + img_object['width']) / 2 / image_width
        width_normalized = img_object['width'] / image_width
        height_normalized = img_object['height'] / image_height

        next_line = '{} {} {} {} {}'.format(img_object['class'], x_center_normalized, y_center_normalized, width_normalized, height_normalized)
        file_content += next_line + '\n'

    path = image_path + '/{}.txt'.format(image.split('.')[0])
    with open(path, 'w') as f:
        f.write(file_content)





