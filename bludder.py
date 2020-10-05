import yaml, json

class bludder:
    def __init__(self):
        self.drapa = {'a': 1, 6: 23}

    def yaml(self):
        return yaml.dump(self)

    def json(self):
        return json.dumps(self)


apa = bludder()
print(apa.yaml())
print(apa.json())



