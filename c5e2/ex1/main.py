import yaml
import colored as cld

def print_yml(yaml_path):
    with open(yaml_path) as open_yaml:
        docs = yaml.full_load(open_yaml)
        for key, val in docs.items():
            color_key = ((cld.fg(14) + cld.bg(17) + cld.attr(4)) + key + cld.attr(0))
            # color_val = () + val + cld.attr(0)
            print(color_key, val)

def run():
    print_yml('../data/potato_salad.yml')

if __name__ == "__main__":
    run()