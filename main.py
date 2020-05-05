import argparse
import duolingo
from DuolingoNagger import DuolingoNagger, ret_duolingo_obj
import time
import argparse

NAG_INTERVAL_SEC = 10

def arg_parse_nagger():
    parser = argparse.ArgumentParser(description = '')
    parser.add_argument('-n', '--nagger', dest='nagger', help='Wanted nagger. Options are: duolingo', required=True)

    return parser.parse_known_args()

def get_conf_nagger():
    args = arg_parse_nagger()[0] # parse_known_args returns a tuple, with all the args not recognized by the current argparse
    switcher = {
        'duolingo': ret_duolingo_obj,
    }
    func = switcher.get(args.nagger, "Invalid nagger")
    return func()
    

if __name__ == "__main__":
    nagger = get_conf_nagger()
    while(True):
        if (nagger.should_nag()):
            nagger.nag()
            time.sleep(NAG_INTERVAL_SEC)