def get(key):
    keys = {}
    with open('.env', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split('=')
            keys[line[0]] = line[1].replace('\n','')
    return (keys[key] if(key in keys.keys()) else None)