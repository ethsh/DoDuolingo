import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
from DuolingoNagger import DuolingoNagger, ret_duolingo_obj
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
    

class PythonCornerExample(SMWinservice):
    _svc_name_ = "PythonCornerExample"
    _svc_display_name_ = "Python Corner's Winservice Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.nagger = get_conf_nagger()
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        pass
"""         while(True):
            if (self.nagger.should_nag()):
                self.nagger.nag()
                time.sleep(NAG_INTERVAL_SEC)
 """
