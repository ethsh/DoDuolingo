'''
An "interface" for a nagger - implements everything in order to nag you to do something
'''
import abc

class INagger(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def should_nag(self):
        raise NotImplementedError('users must define should_nag to use this base class')

    @abc.abstractmethod
    def nag(self):
        raise NotImplementedError('users must define nag to use this base class')