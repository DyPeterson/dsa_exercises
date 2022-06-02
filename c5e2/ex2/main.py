import randomname as rn
import argparse

# name = rn.get_name()
# print(name)
def set_args():
    """
    define arguments for command line
    """
    parser = argparse.ArgumentParser(description="Random name docker parser")
    parser.add_argument('--num-rows', '-n', type=int, help='Number of rows to print')
    parser.add_argument('--output-file')