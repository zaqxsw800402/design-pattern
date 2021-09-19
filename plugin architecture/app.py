import yaml

data = yaml.safe_load(open('data.yaml'))
print(data['plugin'])