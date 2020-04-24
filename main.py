import argparse
import duolingo

def parse_args():
    parser = argparse.ArgumentParser(description = '')
    parser.add_argument('-u', '--user', dest='user', help='your Doulingo user name', required=True)
    parser.add_argument('-p', '--pass', dest='password', help='your Doulingo password', required=True)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    lingo = duolingo.Duolingo(args.user, args.password)
    
    #parser = argparse.ArgumentParser()
    #parser.parse_args()
