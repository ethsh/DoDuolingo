from INagger import INagger
import duolingo
import argparse
import abc

class DuolingoNagger(INagger):
    def __init__(self):
        args = DuolingoNagger.parse_args()
        self.duolingo_user = args.user
        self.duolingo_pass = args.password
        self.duolingo_obj = duolingo.Duolingo(self.duolingo_user, self.duolingo_pass)

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description = '')
        parser.add_argument('-u', '--user', dest='user', help='your Doulingo user name', required=True)
        parser.add_argument('-p', '--pass', dest='password', help='your Doulingo password', required=True)

        return parser.parse_args()

    def should_nag(self):
        daily_xp = self.duolingo_obj.get_daily_xp_progress()
        return daily_xp['xp_goal'] > daily_xp['xp_today']

    def nag(self):
        raise NotImplementedError('users must define nag to use this base class')