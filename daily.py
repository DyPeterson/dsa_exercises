import argparse
def num_dub():
    parser = argparse.ArgumentParser(description="placeholder")
    parser.add_argument('--double', '-d', type=int, help="number to double")
    parser.add_argument('--catname', '-cn')
    args, abc = parser.parse_known_args()

    print(abc)
    print(args)

    if abc is not None:
        raise ValueError(f'{abc}: not a valid argument')

    if args.double is not None:
        double = args.double * 2
        print(double)

num_dub()