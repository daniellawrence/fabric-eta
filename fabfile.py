#!/usr/bin/env python
from fabric.api import task
from eta import print_eta
import time


@print_eta
@task
def sleep5():
    time.sleep(2)
    pass


@print_eta
@task
def sleep1():
    time.sleep(1)
    pass


@print_eta
@task
def sleep3():
    time.sleep(3)
    pass


if __name__ == '__main__':

    sleep1()
    sleep5()
    sleep1()
    sleep5()
    sleep1()
    sleep5()
    sleep3()
    sleep3()
    sleep3()
    sleep3()
