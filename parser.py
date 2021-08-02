import json

def binary_to_json(binary_data):
    string = binary_data.decode()
    string = string.replace('{\'', '{\"')
    string = string.replace('\'}', '\"}')
    string = string.replace('\': \'', '\": \"')
    string = string.replace('\', \'', '\", \"')
    return json.loads(string)
