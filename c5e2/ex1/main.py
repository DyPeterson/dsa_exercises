import yaml

def print_yml(yaml_path):
    with open(yaml_path) as open_yaml:
        docs = yaml.full_load(open_yaml)
        for key, val in docs.items():
            print(key, val)

def run():
    print_yml('../data/potato_salad.yml')

if __name__ == "__main__":
    run()