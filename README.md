## <div align="center">Argus: Low Cost Computation Method for Monocular Distance Estimation in UAV's</div>

Argus allows you to estimate the distance of objects from the drone (or any UAV) from only video footage. It uses out of the box YOLOv5 vision AI software and applies a distance estimation calculation to detected objects. 

Given the drone's altitude, camera angle, camera configurations, and object's bounding box, Argus can estimate the distance of the object to the UAV. 

## How to use Argus
Object detection is ready to go out of the box. It is currently trained on detecting cars and people (weights provided in `au-air.pt`), but the weights can be replaced and trained with anything. 

Run `detect.py` on any image just as if you were using YOLOv5 out of the box. Refer to YOLOv5's official documentation on how to run YOLOv5. 

## Object detection calculation 
The object detection calculation is done in [yolov5/detect.py](yolov5/detect.py) with function `distance_estimation`

```
def distance_estimation(bbox, altitude=60, cam_angle=20, cam_config=dji_mavic_3): 
    x_min = bbox['x1']
    y_min = bbox['y1']
    x_max = bbox['x2']
    y_max = bbox['y2']

    x_f = (x_min + x_max) / 2
    y_f = y_max
    
    x_c = int(cam_config['image_width'] / 2)
    y_c = int(cam_config['image_height'] / 2)

    f_pixel = (cam_config['focal_length'] / cam_config['sensor_width']) * cam_config['image_width'] # focal length in pixels
    cam_angle = math.radians(cam_angle)
    
    h = altitude / math.cos(cam_angle) 
    theta = math.atan((x_c - x_f) / (y_f - y_c))
    
    if(x_f < x_c and y_f < y_c): # quadrant 3
        theta = theta + 3 * math.pi / 2
    elif(x_f > x_c and y_f < y_c): # quadrant 2 
        theta = theta + 3 * math.pi / 2
    elif(x_f > x_c and y_f > y_c): # quadrant 1
        theta = theta + math.pi / 2
    else:                           #quadrant 4
        theta = theta + math.pi / 2
    
    delta = math.atan((math.sqrt((x_f - x_c)**2 + (y_f - y_c)**2)) / f_pixel)
    alpha = math.atan(cam_angle)
    r_prime = h * math.tan(delta) / (1 + alpha * math.cos(theta) * math.tan(delta))
    z_prime = alpha * math.sin(theta) * r_prime
    
    distance = math.sqrt(r_prime**2 + (h - z_prime)**2)
    
    return distance, theta
```