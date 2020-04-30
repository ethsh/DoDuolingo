import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
from DuolingoNagger import DuolingoNagger, ret_duolingo_obj
import argparse
import time


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
    


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self,args):
        print('__init__!')
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        print('SvcDoRun!')
        self.nagger = get_conf_nagger()
        self.main()

    def main(self):
        pass
"""         print('main!')
        while(True):
            if (self.nagger.should_nag()):
                self.nagger.nag()
                time.sleep(NAG_INTERVAL_SEC)
 """

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
