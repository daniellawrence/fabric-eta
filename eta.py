#!/usr/bin/env python
import time
import thread
from blessings import Terminal

LAST_TIME = {}


def _print_eta(f_name, est_time):
    print "est_time: %s" % est_time

    i = 0
    while i < est_time:
        i += .5
        term = Terminal()
        with term.location(0, 0):
            print 'ETA: %.1f' % (est_time - i)
        time.sleep(0.5)
    return


class print_eta(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __call__(self, *args, **kwargs):
        f_name = self.wrapped.__name__
        start = time.time()

        last_time_eta = 10
        if f_name in LAST_TIME:
            last_time_eta = LAST_TIME[f_name]
        thread.start_new_thread(_print_eta, (f_name, last_time_eta))
        x = self.wrapped(*args, **kwargs)
        end = time.time()
        LAST_TIME[f_name] = int(end-start)
        return x
