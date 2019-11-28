import argparse
from cyclops.cyclops import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cyclops - Optimise your AWS.')
    parser.add_argument('--profile', help='The AWS profile to optimise.', required=True)
    args = parser.parse_args()

    main(args.profile)
