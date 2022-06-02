import yaml
import colored as cld

def print_yml(yaml_path):
    with open(yaml_path) as open_yaml:
        docs = yaml.full_load(open_yaml)
        ingredients = docs['ingredients']
        instructions = docs['instructions']
        notes = docs['notes']
        nutrition = docs['nutrition']
        # for key, val in nutrition.items():
        #     color_key = ((cld.fg(14) + cld.bg(17) + cld.attr(4)) + key + cld.attr(0))
        #     print(color_key, color_key2)
        print((notes + cld.fg(30)))
def run():
    print_yml('../data/potato_salad.yml')

if __name__ == "__main__":
    run()