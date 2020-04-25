import argparse
import duolingo
from DuolingoNagger import DuolingoNagger

if __name__ == "__main__":
    nagger = DuolingoNagger()
    print(nagger.should_nag())
    if (nagger.should_nag()):
        nagger.nag()