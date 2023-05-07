import json

f = open('../au-air/training_test_set.json')
data = json.load(f)
print(data['test_set'])