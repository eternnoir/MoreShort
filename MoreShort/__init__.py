# -*- coding: utf-8 -*-
__author__ = 'eternnoir'

from . import googl


def getShortService(serviceName):
    if(serviceName is 'googl'):
        return googl.Googl()
    else:
        raise
