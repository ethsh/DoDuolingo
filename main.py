import argparse
import duolingo
from DuolingoNagger import DuolingoNagger
import time

IDLE_BETWEEN_NAGS = 30

if __name__ == "__main__":
    nagger = DuolingoNagger()
    if (nagger.should_nag()):
        nagger.nag()
        time.sleep(IDLE_BETWEEN_NAGS)