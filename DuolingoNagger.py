from INagger import INagger
import duolingo
import argparse
import abc
from win32gui import GetWindowText, GetForegroundWindow
import ctypes  # An included library with Python install.
import datetime
import time

def raise_(ex):
    raise ex

def ret_duolingo_obj():
    return DuolingoNagger()

class DuolingoNagger(INagger):
    def __init__(self):
        args = DuolingoNagger.parse_args()[0] # parse_known_args returns a tuple, with all the args not recognized by the current argparse
        self.duolingo_user = args.user
        self.duolingo_pass = args.password

        temp_var_nag_time = time.strptime(args.time, '%H%M')
        self.start_nagging_time = datetime.time(temp_var_nag_time.tm_hour, temp_var_nag_time.tm_min)

        self.duolingo_obj = duolingo.Duolingo(self.duolingo_user, self.duolingo_pass)

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description = '')
        parser.add_argument('-u', '--user', dest='user', help='your Doulingo user name', required=True)
        parser.add_argument('-p', '--pass', dest='password', help='your Doulingo password', required=True)
        parser.add_argument('-t', '--time', dest='time', help='When to start nagging in 4 digits (ex. 2130)', required=True,
            type=lambda x: x if (x.isdigit() and len(x) == 4) else raise_(Exception('Invalid time type')))

        return parser.parse_known_args()

    def should_nag(self):
        # check time of day
        if datetime.datetime.now().time() < self.start_nagging_time:
            return False

        # check if Duolingo is currently open
        win_text = GetWindowText(GetForegroundWindow())
        if 'Duolingo' in win_text:
            return False

        # check from daily goal
        streak_info = self.duolingo_obj.get_streak_info()
        return not streak_info['streak_extended_today']

    def nag(self):
        return ctypes.windll.user32.MessageBoxW(0, 'Do Your Doulingo!', 'STOOPID!', 0x1000)